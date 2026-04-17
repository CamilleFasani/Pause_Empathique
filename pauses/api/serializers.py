from rest_framework import serializers

from pauses.models import Feeling, Need, Pause


class FeelingSerializer(serializers.ModelSerializer):
    names = serializers.SerializerMethodField()

    def get_names(self, obj):
        return {
            "f": obj.feminine_name,
            "m": obj.masculine_name,
        }

    class Meta:
        model = Feeling
        fields = ["id", "feeling_family", "names"]


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
            "title",
            "created_at",
            "updated_at",
            "empty_your_bag",
            "observation",
            "feelings",
            "needs",
        ]
        read_only_fields = ["created_at", "updated_at"]
