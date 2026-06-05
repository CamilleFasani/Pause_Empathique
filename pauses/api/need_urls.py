from django.urls import path

from .views import NeedsListView

app_name = "needs"

urlpatterns = [
    path("", NeedsListView.as_view(), name="list"),
]
