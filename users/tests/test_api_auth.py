from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.api.serializers import RegisterSerializer

User = get_user_model()
REFRESH_COOKIE_NAME = "refresh_token"
REFRESH_COOKIE_PATH = "/api/v1/auth/"


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

    def test_common_password_is_rejected(self):
        # Given registration data with a weak/common password
        data = {
            "email": "martin@test.fr",
            "password": "password",
            "firstname": "Martin",
            "gender": "M",
        }

        # When the serializer validates the data
        serializer = RegisterSerializer(data=data)

        # Then the password is rejected before creating a user
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)


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


class LoginAPITest(APITestCase):
    def setUp(self):
        self.url = reverse("api:auth:login")
        self.user = User.objects.create_user(
            email="magda@test.fr",
            password="motdepasse456",
            firstname="Magdalena",
            gender="F",
        )

    def test_login_valid_credentials(self):
        # Given valid credentials
        payload = {"email": "magda@test.fr", "password": "motdepasse456"}

        # When the user logs in
        response = self.client.post(self.url, payload, format="json")

        # Then we get 200 with the access token in the JSON response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertNotIn("refresh", response.data)

        # And the refresh token is stored in an HttpOnly cookie
        self.assertIn(REFRESH_COOKIE_NAME, response.cookies)
        refresh_cookie = response.cookies[REFRESH_COOKIE_NAME]
        self.assertTrue(refresh_cookie.value)
        self.assertTrue(refresh_cookie["httponly"])
        self.assertEqual(refresh_cookie["path"], REFRESH_COOKIE_PATH)
        self.assertIn(refresh_cookie["samesite"], ["Lax", "None"])

    def test_login_wrong_password(self):
        # Given wrong password
        payload = {"email": "magda@test.fr", "password": "mauvaismdp"}

        # When the user tries to log in
        response = self.client.post(self.url, payload, format="json")

        # Then access is denied and no refresh cookie is created
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn(REFRESH_COOKIE_NAME, response.cookies)

    def test_login_unknown_email(self):
        # Given an email that doesn't exist in the database
        payload = {"email": "inconnu@test.fr", "password": "motdepasse456"}

        # When the user tries to log in
        response = self.client.post(self.url, payload, format="json")

        # Then access is denied and no refresh cookie is created
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn(REFRESH_COOKIE_NAME, response.cookies)


class RefreshTokenAPITest(APITestCase):
    def setUp(self):
        self.login_url = reverse("api:auth:login")
        self.refresh_url = reverse("api:auth:token_refresh")
        self.user = User.objects.create_user(
            email="magda@test.fr",
            password="motdepasse456",
            firstname="Magdalena",
            gender="F",
        )

    def _login(self):
        """Helper : login and keep the refresh cookie in the test client."""
        return self.client.post(
            self.login_url,
            {"email": "magda@test.fr", "password": "motdepasse456"},
            format="json",
        )

    def test_refresh_uses_cookie_and_returns_access_token(self):
        # Given a logged-in user with a refresh token stored in an HttpOnly cookie
        login_response = self._login()
        self.assertIn(REFRESH_COOKIE_NAME, login_response.cookies)

        # When the client refreshes the access token without sending a JSON body
        response = self.client.post(self.refresh_url, format="json")

        # Then a new access token is returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

        # And the refresh token is not exposed in the JSON response
        self.assertNotIn("refresh", response.data)

    def test_refresh_without_cookie_is_rejected(self):
        # Given an unauthenticated client without a refresh cookie

        # When the client tries to refresh the access token
        response = self.client.post(self.refresh_url, format="json")

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_invalid_cookie_is_rejected(self):
        # Given a client with an invalid refresh cookie
        self.client.cookies[REFRESH_COOKIE_NAME] = "tokeninvalide"

        # When the client tries to refresh the access token
        response = self.client.post(self.refresh_url, format="json")

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class LogoutAPITest(APITestCase):
    def setUp(self):
        self.login_url = reverse("api:auth:login")
        self.logout_url = reverse("api:auth:token_blacklist")
        self.refresh_url = reverse("api:auth:token_refresh")
        self.user = User.objects.create_user(
            email="magda@test.fr",
            password="motdepasse456",
            firstname="Magdalena",
            gender="F",
        )

    def _login(self):
        """Helper : login and keep the refresh cookie in the test client."""
        return self.client.post(
            self.login_url,
            {"email": "magda@test.fr", "password": "motdepasse456"},
            format="json",
        )

    def test_logout_blacklists_refresh_cookie_token(self):
        # Given a logged-in user with a valid refresh token in an HttpOnly cookie
        login_response = self._login()
        refresh = login_response.cookies[REFRESH_COOKIE_NAME].value

        # When they log out
        response = self.client.post(self.logout_url, format="json")

        # Then the logout succeeds
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # And the refresh cookie is deleted by the response
        self.assertIn(REFRESH_COOKIE_NAME, response.cookies)
        deleted_cookie = response.cookies[REFRESH_COOKIE_NAME]
        self.assertEqual(deleted_cookie.value, "")
        self.assertEqual(deleted_cookie["max-age"], 0)

        # And the refresh token can no longer be used to get a new access token
        self.client.cookies[REFRESH_COOKIE_NAME] = refresh
        refresh_response = self.client.post(self.refresh_url, format="json")
        self.assertEqual(refresh_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_without_cookie_is_rejected(self):
        # Given an unauthenticated client without a refresh cookie

        # When they try to log out
        response = self.client.post(self.logout_url, format="json")

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_invalid_cookie_token(self):
        # Given a client with a malformed / invalid refresh cookie
        self.client.cookies[REFRESH_COOKIE_NAME] = "tokeninvalide"

        # When we try to blacklist it
        response = self.client.post(self.logout_url, format="json")

        # Then we get a 401 (Simple JWT rejects the token as unauthorized)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


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

        # Then they get their data back - without password
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
            self.url, {"firstname": "Camillette"}, format="json"
        )

        # Then the update is persisted
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["firstname"], "Camillette")
        self.user.refresh_from_db()
        self.assertEqual(self.user.firstname, "Camillette")

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
