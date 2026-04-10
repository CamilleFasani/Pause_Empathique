from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.api.serializers import RegisterSerializer

User = get_user_model()


class RegisterSerializerTest(APITestCase):
    """Tests unitaires du serializer — pas de requête HTTP."""

    def test_password_is_hashed_on_create(self):
        # Given valid data
        data = {
            "email": "martin@test.fr",
            "password": "motdepasse123",
            "firstname": "Martin",
            "gender": "M",
        }

        # When the serializer creates the user
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        # Then the password is hashed, never stored in plain text
        self.assertNotEqual(user.password, "motdepasse123")
        self.assertTrue(user.check_password("motdepasse123"))

    def test_password_is_write_only(self):
        # Given a valid user created via the serializer
        data = {
            "email": "martin@test.fr",
            "password": "motdepasse123",
            "firstname": "Martin",
            "gender": "M",
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        # Then the password does not appear in the serialized output
        self.assertNotIn("password", serializer.data)


class RegisterAPITest(APITestCase):
    def setUp(self):
        self.url = reverse("api:auth:register")
        self.valid_data = {
            "email": "martin@test.fr",
            "password": "motdepasse123",
            "firstname": "Martin",
            "gender": "M",
        }

    def test_register_valid_data(self):
        # Given valid data from a user
        payload = self.valid_data

        # When the user clicks on register
        response = self.client.post(self.url, payload, format="json")

        # Then the user is created and we return 201 with the user data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], payload["email"])
        self.assertEqual(response.data["firstname"], payload["firstname"])
        self.assertEqual(response.data["gender"], payload["gender"])
        self.assertNotIn("password", response.data)

    def test_register_invalid_email(self):
        # Given invalid email data
        payload = self.valid_data.copy()
        payload["email"] = "invalid-email"

        # When the user clicks on register
        response = self.client.post(self.url, payload, format="json")

        # Then we return 400 with error message
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_register_duplicate_email(self):
        # Given an existing user with the same email
        User.objects.create_user(**self.valid_data)

        # When another user tries to register with the same email
        payload = self.valid_data.copy()
        payload["firstname"] = "Another"
        response = self.client.post(self.url, payload, format="json")

        # Then we return 400 with error message about duplicate email
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_register_missing_fields(self):
        # Given missing required fields
        payload = {
            "email": "",
            "password": "",
            "firstname": "Siloë",
            "gender": "F",
        }

        # When the user clicks on register
        response = self.client.post(self.url, payload, format="json")

        # Then we return 400 with error message about missing fields
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
        self.assertIn("password", response.data)


# class LoginAPITest(APITestCase):
#     def setUp(self):
#         self.url = reverse("auth:login")
#         self.user = User.objects.create_user(
#             email="camille@test.fr",
#             password="motdepasse123",
#             firstname="Camille",
#             gender="F",
#         )

#     def test_login_valid_credentials(self):
#         # POST valide → 200, contient "access" et "refresh"
#         ...

#     def test_login_wrong_password(self):
#         # POST mauvais mdp → 401
#         ...

#     def test_login_unknown_email(self):
#         # POST email inconnu → 401
#         ...


class UserMeAPITest(APITestCase):
    def setUp(self):
        self.url = reverse("api:users:me")
        self.user = User.objects.create_user(
            email="camille@test.fr",
            password="motdepasse123",
            firstname="Camille",
            gender="F",
        )

    def test_get_profile_authenticated(self):
        # Given an authenticated user
        self.client.force_authenticate(user=self.user)

        # When they request their profile
        response = self.client.get(self.url)

        # Then they get their data back
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)
        self.assertEqual(response.data["firstname"], self.user.firstname)
        self.assertNotIn("password", response.data)

    def test_get_profile_unauthenticated(self):
        # Given an unauthenticated client (no token)

        # When they request the profile endpoint
        response = self.client.get(self.url)

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_profile(self):
        # Given an authenticated user
        self.client.force_authenticate(user=self.user)

        # When they update their firstname
        response = self.client.patch(
            self.url, {"firstname": "Camille M."}, format="json"
        )

        # Then the update is persisted
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["firstname"], "Camille M.")
        self.user.refresh_from_db()
        self.assertEqual(self.user.firstname, "Camille M.")

    def test_patch_profile_unauthenticated(self):
        # Given an unauthenticated client

        # When they try to update a profile
        response = self.client.patch(self.url, {"firstname": "Hacker"}, format="json")

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_account(self):
        # Given an authenticated user
        self.client.force_authenticate(user=self.user)

        # When they delete their account
        response = self.client.delete(self.url)

        # Then the account is removed from the database
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(email="camille@test.fr").exists())

    def test_delete_account_unauthenticated(self):
        # Given an unauthenticated client

        # When they try to delete an account
        response = self.client.delete(self.url)

        # Then access is denied and no user is deleted
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(User.objects.filter(email="camille@test.fr").exists())
