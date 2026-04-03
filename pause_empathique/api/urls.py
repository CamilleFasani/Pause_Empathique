from django.urls import include, path

from .views import HealthCheckView

app_name = "api"

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path("users/", include("users.api.user_urls", namespace="users")),
    path("auth/", include("users.api.auth_urls", namespace="auth")),
]
