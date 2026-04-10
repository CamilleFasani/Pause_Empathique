from django.urls import path

from users.api.views import UserMeAPIView

app_name = "users"

urlpatterns = [
    path("me/", UserMeAPIView.as_view(), name="me"),
]
