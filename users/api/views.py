from django.conf import settings
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from .serializers import (
    AccessTokenResponseSerializer,
    AuthDetailResponseSerializer,
    RegisterSerializer,
    UserSerializer,
)


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CookieTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    @extend_schema(
        responses={
            200: OpenApiResponse(
                response=AccessTokenResponseSerializer,
                description=(
                    "Access token returned in JSON. The refresh token is set in "
                    "an HttpOnly cookie and is not exposed in the response body."
                ),
            ),
            401: OpenApiResponse(description="Invalid credentials."),
        },
        description=(
            "Authenticate a user. On success, returns an access token and sets "
            "the refresh token in the HttpOnly refresh cookie."
        ),
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code != status.HTTP_200_OK:
            return response

        refresh_token = response.data.pop("refresh")
        response.set_cookie(
            key=settings.REFRESH_COOKIE_NAME,
            value=refresh_token,
            httponly=True,
            secure=settings.REFRESH_COOKIE_SECURE,
            samesite=settings.REFRESH_COOKIE_SAMESITE,
            path=settings.REFRESH_COOKIE_PATH,
            max_age=settings.REFRESH_COOKIE_MAX_AGE,
        )

        return response


class CookieTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(
                response=AccessTokenResponseSerializer,
                description=(
                    "New access token returned in JSON. The refresh token is "
                    "read from the HttpOnly refresh cookie."
                ),
            ),
            401: OpenApiResponse(
                response=AuthDetailResponseSerializer,
                description="Missing, invalid, expired, or blacklisted refresh cookie.",
            ),
        },
        description=(
            "Refresh the access token using the HttpOnly refresh cookie. No "
            "refresh token is expected in the request body."
        ),
    )
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get(settings.REFRESH_COOKIE_NAME)
        if not refresh_token:
            return Response(
                {"detail": "Refresh token not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        serializer = self.get_serializer(data={"refresh": refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as error:
            raise InvalidToken(error.args[0]) from error

        response = Response(serializer.validated_data, status=status.HTTP_200_OK)

        if "refresh" in response.data:
            new_refresh_token = response.data.pop("refresh")
            response.set_cookie(
                key=settings.REFRESH_COOKIE_NAME,
                value=new_refresh_token,
                httponly=True,
                secure=settings.REFRESH_COOKIE_SECURE,
                samesite=settings.REFRESH_COOKIE_SAMESITE,
                path=settings.REFRESH_COOKIE_PATH,
                max_age=settings.REFRESH_COOKIE_MAX_AGE,
            )

        return response


class CookieTokenBlacklistView(TokenBlacklistView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(
                description="Refresh token blacklisted and cookie deleted."
            ),
            401: OpenApiResponse(
                response=AuthDetailResponseSerializer,
                description="Missing, invalid, expired, or blacklisted refresh cookie.",
            ),
        },
        description=(
            "Log out using the HttpOnly refresh cookie. No refresh token is "
            "expected in the request body."
        ),
    )
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get(settings.REFRESH_COOKIE_NAME)
        if not refresh_token:
            return Response(
                {"detail": "Refresh token not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        serializer = self.get_serializer(data={"refresh": refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as error:
            raise InvalidToken(error.args[0]) from error

        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie(
            settings.REFRESH_COOKIE_NAME, path=settings.REFRESH_COOKIE_PATH
        )

        return response


class UserMeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
