from django.urls import path

from users.api.views import (
    CookieTokenBlacklistView,
    CookieTokenObtainPairView,
    CookieTokenRefreshView,
    RegisterAPIView,
)

app_name = "auth"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("token/", CookieTokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),
    path(
        "token/blacklist/",
        CookieTokenBlacklistView.as_view(),
        name="token_blacklist",
    ),
]
