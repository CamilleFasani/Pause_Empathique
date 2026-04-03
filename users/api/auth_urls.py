from django.urls import path

app_name = "auth"

urlpatterns = [
    path("register/", name="register"),
    path("token/", name="login"),
    path("token/refresh/", name="token_refresh"),
    path("token/blacklist/", name="token_blacklist"),
]
