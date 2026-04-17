from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from pauses.api.serializers import PauseSerializer
from pauses.models import Feeling, Need, Pause

User = get_user_model()


class PauseSerializerReadTest(TestCase):
    """Tests unitaires de sérialisation (lecture) — SER-01 à SER-05."""

    def setUp(self):
        self.user = User.objects.create_user(
            email="alice@test.fr",
            password="motdepasse123",
            firstname="Alice",
            gender="F",
        )
        self.feeling = Feeling.objects.create(
            feeling_family=Feeling.FeelingFamily.TENSION,
            feminine_name="submergée",
            masculine_name="submergé",
        )
        self.need = Need.objects.create(
            need_family=Need.NeedFamily.SURVIE,
            name="sécurité",
        )
        self.pause = Pause.objects.create(
            user=self.user,
            title="Ma pause",
            empty_your_bag="bag",
            observation="obs",
        )
        self.pause.feelings.add(self.feeling)
        self.pause.needs.add(self.need)

    def test_feelings_structure_names(self):
        # SER-01
        # Given a pause with one feeling
        serializer = PauseSerializer(instance=self.pause)

        # When the pause is serialized
        data = serializer.data

        # Then the feeling exposes a `names` dict with `f` and `m` keys
        self.assertEqual(len(data["feelings"]), 1)
        self.assertEqual(
            data["feelings"][0]["names"],
            {"f": "submergée", "m": "submergé"},
        )

    def test_needs_structure_name(self):
        # SER-02
        # Given a pause with one need
        serializer = PauseSerializer(instance=self.pause)

        # When the pause is serialized
        data = serializer.data

        # Then the need exposes a `name` field
        self.assertEqual(len(data["needs"]), 1)
        self.assertEqual(data["needs"][0]["name"], "sécurité")

    def test_user_field_absent_from_output(self):
        # SER-03
        # Given a pause linked to a user
        serializer = PauseSerializer(instance=self.pause)

        # When the pause is serialized
        data = serializer.data

        # Then the `user` key is not exposed in the response
        self.assertNotIn("user", data)

    def test_all_expected_fields_present(self):
        # SER-05
        # Given a complete pause
        serializer = PauseSerializer(instance=self.pause)

        # When the pause is serialized
        data = serializer.data

        # Then the response contains exactly the expected keys
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
        self.assertEqual(set(data.keys()), expected_keys)


class PauseSerializerWriteTest(TestCase):
    """Tests unitaires de validation (écriture) — SER-06 à SER-09."""

    def setUp(self):
        self.user = User.objects.create_user(
            email="alice@test.fr",
            password="motdepasse123",
            firstname="Alice",
            gender="F",
        )
        self.feeling = Feeling.objects.create(
            feeling_family=Feeling.FeelingFamily.JOIE,
            feminine_name="Heureuse",
            masculine_name="Heureux",
        )
        self.need = Need.objects.create(
            need_family=Need.NeedFamily.HARMONIE,
            name="Paix",
        )

    def test_minimal_valid_payload(self):
        # SER-06
        # Given a minimal valid payload (feelings + needs)
        data = {
            "feelings": [self.feeling.id],
            "needs": [self.need.id],
        }

        # When the serializer is validated
        serializer = PauseSerializer(data=data)

        # Then it is valid
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)

    def test_title_auto_generated_when_absent(self):
        # SER-07
        # Given a payload without `title`
        data = {
            "feelings": [self.feeling.id],
            "needs": [self.need.id],
        }

        # When the serializer is validated and saved (user passed at save time)
        serializer = PauseSerializer(data=data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)
        pause = serializer.save(user=self.user)

        # Then the title matches the auto-generated format "Pause du JJ Mois AAAA"
        months_in_french = {
            1: "Janvier",
            2: "Février",
            3: "Mars",
            4: "Avril",
            5: "Mai",
            6: "Juin",
            7: "Juillet",
            8: "Août",
            9: "Septembre",
            10: "Octobre",
            11: "Novembre",
            12: "Décembre",
        }
        now = timezone.now()
        expected_title = f"Pause du {now.day} {months_in_french[now.month]} {now.year}"
        self.assertEqual(pause.title, expected_title)

    def test_title_too_long_is_rejected(self):
        # SER-08
        # Given a title exceeding 200 characters
        data = {
            "title": "a" * 201,
            "feelings": [self.feeling.id],
            "needs": [self.need.id],
        }

        # When the serializer is validated
        serializer = PauseSerializer(data=data)

        # Then it is invalid and the error points to `title`
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_feelings_and_needs_required(self):
        # SER-09
        # Given a payload without feelings nor needs
        data = {
            "title": "Ma pause",
        }

        # When the serializer is validated
        serializer = PauseSerializer(data=data)

        # Then it is invalid with errors on both `feelings` and `needs`
        self.assertFalse(serializer.is_valid())
        self.assertIn("feelings", serializer.errors)
        self.assertIn("needs", serializer.errors)
