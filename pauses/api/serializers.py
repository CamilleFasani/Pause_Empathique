from rest_framework import serializers

from pauses.models import Feeling, Need, Pause


class FeelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeling
        fields = ["id", "feeling_family", "feminine_name", "masculine_name"]


class NeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Need
        fields = ["id", "need_family", "name"]


class PauseSerializer(serializers.ModelSerializer):
    feelings = FeelingSerializer(many=True, read_only=True)
    needs = NeedSerializer(many=True, read_only=True)

    class Meta:
        model = Pause
        fields = [
            "id",
            "user",
            "title",
            "created_at",
            "updated_at",
            "empty_your_bag",
            "observation",
            "feelings",
            "needs",
        ]
        read_only_fields = ["user", "created_at", "updated_at"]
