from django.urls import path
from .views import (
    CustomLoginView,
    UserProfileUpdateView,
    UserProfileView,
    UserProfileDeleteView,
)
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/update/", UserProfileUpdateView.as_view(), name="update_profile"),
    path("profile/delete/", UserProfileDeleteView.as_view(), name="delete_profile"),
]
