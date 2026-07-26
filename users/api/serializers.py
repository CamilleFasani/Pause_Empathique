from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

from users.models import User


class AccessTokenResponseSerializer(serializers.Serializer):
    access = serializers.CharField()


class AuthDetailResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = ["email", "password", "firstname", "gender"]

    def validate(self, attrs):
        user = User(
            email=attrs["email"],
            firstname=attrs["firstname"],
            gender=attrs["gender"],
        )

        try:
            validate_password(attrs["password"], user=user)
        except DjangoValidationError as error:
            raise serializers.ValidationError({"password": error.messages}) from error

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "firstname", "gender", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
