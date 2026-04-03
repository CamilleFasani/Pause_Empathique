from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "firstname", "gender"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "firstname", "gender", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
