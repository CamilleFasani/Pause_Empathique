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
    # validation des ids de feelings et needs à la création ou mise à jour d'une pause
    # donc en écriture
    feelings = serializers.PrimaryKeyRelatedField(
        many=True, allow_empty=False, queryset=Feeling.objects.all()
    )
    needs = serializers.PrimaryKeyRelatedField(
        many=True, allow_empty=False, queryset=Need.objects.all()
    )

    # structuration des feelings et needs avec les champs nécessaires à l'affichage
    # donc en lecture
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["feelings"] = FeelingSerializer(instance.feelings.all(), many=True).data
        rep["needs"] = NeedSerializer(instance.needs.all(), many=True).data
        return rep

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
