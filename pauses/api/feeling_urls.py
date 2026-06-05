from django.urls import path

from .views import FeelingsListView

app_name = "feelings"

urlpatterns = [
    path("", FeelingsListView.as_view(), name="list"),
]
