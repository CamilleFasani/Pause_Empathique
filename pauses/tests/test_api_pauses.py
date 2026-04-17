from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pauses.models import Feeling, Need, Pause

User = get_user_model()


class PauseListAPITest(APITestCase):
    """GET /api/v1/pauses/ — Liste des pauses de l'utilisateur connecté."""

    def setUp(self):
        self.url = reverse("api:pauses:list")
        self.user_a = User.objects.create_user(
            email="alice@test.fr",
            password="motdepasse123",
            firstname="Alice",
            gender="F",
        )
        self.user_b = User.objects.create_user(
            email="bob@test.fr",
            password="motdepasse456",
            firstname="Bob",
            gender="M",
        )

    def test_list_own_pauses(self):
        # LST-01
        # Given user A authenticated with 3 pauses in DB
        Pause.objects.create(user=self.user_a, title="Pause 1")
        Pause.objects.create(user=self.user_a, title="Pause 2")
        Pause.objects.create(user=self.user_a, title="Pause 3")
        self.client.force_authenticate(user=self.user_a)

        # When they request their list of pauses
        response = self.client.get(self.url)

        # Then they get 200 with 3 pauses, each exposing the expected fields
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        expected_keys = {
            "id",
            "title",
            "created_at",
            "updated_at",
            "empty_your_bag",
            "observation",
            "feelings",
            "needs",
        }
        for pause in response.data:
            self.assertTrue(expected_keys.issubset(set(pause.keys())))

    def test_list_empty(self):
        # LST-02
        # Given user A authenticated with no pauses in DB
        self.client.force_authenticate(user=self.user_a)

        # When they request their list of pauses
        response = self.client.get(self.url)

        # Then they get 200 with an empty list
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_list_isolation_between_users(self):
        # LST-03
        # Given user A authenticated, user B owns 10 pauses
        for i in range(10):
            Pause.objects.create(user=self.user_b, title=f"Pause de Bob #{i}")
        self.client.force_authenticate(user=self.user_a)

        # When user A requests their list
        response = self.client.get(self.url)

        # Then user A sees none of user B's pauses
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_list_unauthenticated(self):
        # LST-04
        # Given no authentication (no Authorization header)

        # When requesting the list
        response = self.client.get(self.url)

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_invalid_token(self):
        # LST-05
        # Given a malformed / invalid bearer token
        self.client.credentials(HTTP_AUTHORIZATION="Bearer tokeninvalide")

        # When requesting the list
        response = self.client.get(self.url)

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PauseCreateAPITest(APITestCase):
    """POST /api/v1/pauses/ — Création d'une pause."""

    def setUp(self):
        self.url = reverse("api:pauses:list")
        self.user_a = User.objects.create_user(
            email="alice@test.fr",
            password="motdepasse123",
            firstname="Alice",
            gender="F",
        )
        self.user_b = User.objects.create_user(
            email="bob@test.fr",
            password="motdepasse456",
            firstname="Bob",
            gender="M",
        )
        self.feeling_1 = Feeling.objects.create(
            feeling_family=Feeling.FeelingFamily.JOIE,
            feminine_name="Heureuse",
            masculine_name="Heureux",
        )
        self.feeling_2 = Feeling.objects.create(
            feeling_family=Feeling.FeelingFamily.AFFECTION,
            feminine_name="Attendrie",
            masculine_name="Attendri",
        )
        self.need_1 = Need.objects.create(
            need_family=Need.NeedFamily.HARMONIE,
            name="Paix",
        )
        self.valid_payload = {
            "title": "Ma pause du jour",
            "empty_your_bag": "Je vide mon sac",
            "observation": "Observation factuelle",
            "feelings": [self.feeling_1.id, self.feeling_2.id],
            "needs": [self.need_1.id],
        }

    def test_create_valid_pause(self):
        # CRE-01
        # Given an authenticated user and a complete valid payload
        self.client.force_authenticate(user=self.user_a)

        # When they create a pause
        response = self.client.post(self.url, self.valid_payload, format="json")

        # Then the pause is created, returned with an id, linked to user A
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["title"], self.valid_payload["title"])
        self.assertEqual(
            response.data["empty_your_bag"], self.valid_payload["empty_your_bag"]
        )
        self.assertEqual(
            response.data["observation"], self.valid_payload["observation"]
        )
        pause = Pause.objects.get(id=response.data["id"])
        self.assertEqual(pause.user, self.user_a)
        self.assertEqual(pause.feelings.count(), 2)
        self.assertEqual(pause.needs.count(), 1)

    def test_create_missing_feelings(self):
        # CRE-02 (variante feelings)
        # Given a payload without any feeling
        self.client.force_authenticate(user=self.user_a)
        payload = self.valid_payload.copy()
        payload["feelings"] = []

        # When they attempt to create the pause
        response = self.client.post(self.url, payload, format="json")

        # Then we return 400 with an error on feelings
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("feelings", response.data)

    def test_create_missing_needs(self):
        # CRE-02 (variante needs)
        # Given a payload without any need
        self.client.force_authenticate(user=self.user_a)
        payload = self.valid_payload.copy()
        payload["needs"] = []

        # When they attempt to create the pause
        response = self.client.post(self.url, payload, format="json")

        # Then we return 400 with an error on needs
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("needs", response.data)

    def test_create_invalid_feeling_id(self):
        # CRE-03
        # Given a payload referencing a non-existent feeling id
        self.client.force_authenticate(user=self.user_a)
        payload = self.valid_payload.copy()
        payload["feelings"] = [9999]

        # When they attempt to create the pause
        response = self.client.post(self.url, payload, format="json")

        # Then we return 400 with an error on feelings
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("feelings", response.data)

    def test_create_title_too_long(self):
        # CRE-04
        # Given a title exceeding 200 characters
        self.client.force_authenticate(user=self.user_a)
        payload = self.valid_payload.copy()
        payload["title"] = "a" * 201

        # When they attempt to create the pause
        response = self.client.post(self.url, payload, format="json")

        # Then we return 400 with an error on title
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_create_unauthenticated(self):
        # CRE-05
        # Given no authentication

        # When creating a pause
        response = self.client.post(self.url, self.valid_payload, format="json")

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_field_is_ignored(self):
        # CRE-06
        # Given user A authenticated, with a body trying to assign the pause to user B
        self.client.force_authenticate(user=self.user_a)
        payload = self.valid_payload.copy()
        payload["user"] = self.user_b.id

        # When they submit the request
        response = self.client.post(self.url, payload, format="json")

        # Then the pause is created but linked to user A (body user field ignored)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        pause = Pause.objects.get(id=response.data["id"])
        self.assertEqual(pause.user, self.user_a)


class PauseDetailAPITest(APITestCase):
    """GET /api/v1/pauses/<id>/ — Détail d'une pause."""

    def setUp(self):
        self.user_a = User.objects.create_user(
            email="alice@test.fr",
            password="motdepasse123",
            firstname="Alice",
            gender="F",
        )
        self.user_b = User.objects.create_user(
            email="bob@test.fr",
            password="motdepasse456",
            firstname="Bob",
            gender="M",
        )
        self.pause = Pause.objects.create(
            user=self.user_a,
            title="Ma pause",
            empty_your_bag="bag",
            observation="obs",
        )
        self.url = reverse("api:pauses:detail", kwargs={"pk": self.pause.pk})

    def test_get_own_pause(self):
        # DET-01
        # Given user A authenticated and owner of the pause
        self.client.force_authenticate(user=self.user_a)

        # When they request the detail
        response = self.client.get(self.url)

        # Then they get 200 with all expected fields
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_keys = {
            "id",
            "title",
            "created_at",
            "updated_at",
            "empty_your_bag",
            "observation",
            "feelings",
            "needs",
        }
        self.assertTrue(expected_keys.issubset(set(response.data.keys())))
        self.assertEqual(response.data["id"], self.pause.id)

    def test_get_nonexistent_pause(self):
        # DET-02
        # Given user A authenticated and a non-existent pause id
        self.client.force_authenticate(user=self.user_a)
        url = reverse("api:pauses:detail", kwargs={"pk": 9999})

        # When they request the detail
        response = self.client.get(url)

        # Then we return 404
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_pause_isolation(self):
        # DET-03
        # Given user A authenticated, but the pause belongs to user B
        pause_b = Pause.objects.create(user=self.user_b, title="Pause de Bob")
        url = reverse("api:pauses:detail", kwargs={"pk": pause_b.pk})
        self.client.force_authenticate(user=self.user_a)

        # When user A tries to access user B's pause
        response = self.client.get(url)

        # Then we return 404 (existence of the pause is not revealed)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_unauthenticated(self):
        # DET-04
        # Given no authentication

        # When requesting the detail
        response = self.client.get(self.url)

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_invalid_token(self):
        # DET-05
        # Given a malformed / invalid bearer token
        self.client.credentials(HTTP_AUTHORIZATION="Bearer tokeninvalide")

        # When requesting the detail
        response = self.client.get(self.url)

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PauseUpdateAPITest(APITestCase):
    """PATCH /api/v1/pauses/<id>/ — Modification partielle d'une pause."""

    def setUp(self):
        self.user_a = User.objects.create_user(
            email="alice@test.fr",
            password="motdepasse123",
            firstname="Alice",
            gender="F",
        )
        self.user_b = User.objects.create_user(
            email="bob@test.fr",
            password="motdepasse456",
            firstname="Bob",
            gender="M",
        )
        self.feeling_1 = Feeling.objects.create(
            feeling_family=Feeling.FeelingFamily.JOIE,
            feminine_name="Heureuse",
            masculine_name="Heureux",
        )
        self.feeling_2 = Feeling.objects.create(
            feeling_family=Feeling.FeelingFamily.AFFECTION,
            feminine_name="Attendrie",
            masculine_name="Attendri",
        )
        self.need_1 = Need.objects.create(
            need_family=Need.NeedFamily.HARMONIE,
            name="Paix",
        )
        self.pause = Pause.objects.create(
            user=self.user_a,
            title="Titre initial",
            empty_your_bag="bag",
            observation="obs",
        )
        self.pause.feelings.add(self.feeling_1)
        self.pause.needs.add(self.need_1)
        self.url = reverse("api:pauses:detail", kwargs={"pk": self.pause.pk})

    def test_patch_title(self):
        # UPD-01
        # Given user A authenticated and owner of the pause
        self.client.force_authenticate(user=self.user_a)

        # When they patch the title
        response = self.client.patch(
            self.url, {"title": "Nouveau titre"}, format="json"
        )

        # Then the update is persisted and the response exposes all fields
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Nouveau titre")
        expected_keys = {
            "id",
            "title",
            "created_at",
            "updated_at",
            "empty_your_bag",
            "observation",
            "feelings",
            "needs",
        }
        self.assertTrue(expected_keys.issubset(set(response.data.keys())))
        self.pause.refresh_from_db()
        self.assertEqual(self.pause.title, "Nouveau titre")

    def test_patch_feelings(self):
        # UPD-02
        # Given user A authenticated and owner of the pause
        self.client.force_authenticate(user=self.user_a)

        # When they patch the feelings with a new set of ids
        response = self.client.patch(
            self.url,
            {"feelings": [self.feeling_1.id, self.feeling_2.id]},
            format="json",
        )

        # Then the M2M is replaced with the new set
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pause.refresh_from_db()
        self.assertEqual(self.pause.feelings.count(), 2)
        feeling_ids = set(self.pause.feelings.values_list("id", flat=True))
        self.assertEqual(feeling_ids, {self.feeling_1.id, self.feeling_2.id})

    def test_patch_title_too_long(self):
        # UPD-03
        # Given a title exceeding 200 characters
        self.client.force_authenticate(user=self.user_a)

        # When they patch the title
        response = self.client.patch(self.url, {"title": "a" * 201}, format="json")

        # Then we return 400 with an error on title
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_patch_invalid_feeling_id(self):
        # UPD-04
        # Given a payload referencing a non-existent feeling id
        self.client.force_authenticate(user=self.user_a)

        # When they patch feelings
        response = self.client.patch(self.url, {"feelings": [9999]}, format="json")

        # Then we return 400 with an error on feelings
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("feelings", response.data)

    def test_patch_nonexistent_pause(self):
        # UPD-05
        # Given user A authenticated and a non-existent pause id
        self.client.force_authenticate(user=self.user_a)
        url = reverse("api:pauses:detail", kwargs={"pk": 9999})

        # When they patch the resource
        response = self.client.patch(url, {"title": "X"}, format="json")

        # Then we return 404
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_pause_isolation(self):
        # UPD-06
        # Given user A authenticated, but the pause belongs to user B
        pause_b = Pause.objects.create(user=self.user_b, title="Pause de Bob")
        url = reverse("api:pauses:detail", kwargs={"pk": pause_b.pk})
        self.client.force_authenticate(user=self.user_a)

        # When user A tries to patch user B's pause
        response = self.client.patch(url, {"title": "Hacker"}, format="json")

        # Then we return 404 and user B's pause is untouched
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        pause_b.refresh_from_db()
        self.assertEqual(pause_b.title, "Pause de Bob")

    def test_patch_unauthenticated(self):
        # UPD-07
        # Given no authentication

        # When patching the pause
        response = self.client.patch(self.url, {"title": "X"}, format="json")

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_invalid_token(self):
        # UPD-08
        # Given a malformed / invalid bearer token
        self.client.credentials(HTTP_AUTHORIZATION="Bearer tokeninvalide")

        # When patching the pause
        response = self.client.patch(self.url, {"title": "X"}, format="json")

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PauseDeleteAPITest(APITestCase):
    """DELETE /api/v1/pauses/<id>/ — Suppression d'une pause."""

    def setUp(self):
        self.user_a = User.objects.create_user(
            email="alice@test.fr",
            password="motdepasse123",
            firstname="Alice",
            gender="F",
        )
        self.user_b = User.objects.create_user(
            email="bob@test.fr",
            password="motdepasse456",
            firstname="Bob",
            gender="M",
        )
        self.pause = Pause.objects.create(
            user=self.user_a,
            title="Pause à supprimer",
        )
        self.url = reverse("api:pauses:detail", kwargs={"pk": self.pause.pk})

    def test_delete_own_pause(self):
        # DEL-01
        # Given user A authenticated and owner of the pause
        self.client.force_authenticate(user=self.user_a)

        # When they delete their pause
        response = self.client.delete(self.url)

        # Then we return 204 and the pause no longer exists in DB
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Pause.objects.filter(pk=self.pause.pk).exists())

    def test_delete_nonexistent_pause(self):
        # DEL-02
        # Given user A authenticated and a non-existent pause id
        self.client.force_authenticate(user=self.user_a)
        url = reverse("api:pauses:detail", kwargs={"pk": 9999})

        # When they try to delete
        response = self.client.delete(url)

        # Then we return 404
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_pause_isolation(self):
        # DEL-03
        # Given user A authenticated, but the pause belongs to user B
        pause_b = Pause.objects.create(user=self.user_b, title="Pause de Bob")
        url = reverse("api:pauses:detail", kwargs={"pk": pause_b.pk})
        self.client.force_authenticate(user=self.user_a)

        # When user A tries to delete user B's pause
        response = self.client.delete(url)

        # Then we return 404 and user B's pause still exists
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(Pause.objects.filter(pk=pause_b.pk).exists())

    def test_delete_unauthenticated(self):
        # DEL-04
        # Given no authentication

        # When trying to delete the pause
        response = self.client.delete(self.url)

        # Then access is denied and the pause still exists
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Pause.objects.filter(pk=self.pause.pk).exists())

    def test_delete_invalid_token(self):
        # DEL-05
        # Given a malformed / invalid bearer token
        self.client.credentials(HTTP_AUTHORIZATION="Bearer tokeninvalide")

        # When trying to delete the pause
        response = self.client.delete(self.url)

        # Then access is denied
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
