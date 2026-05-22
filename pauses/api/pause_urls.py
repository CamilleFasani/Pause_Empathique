from django.urls import path

from .views import PauseDetailView, PauseListCreateView

app_name = "pauses"

urlpatterns = [
    path("", PauseListCreateView.as_view(), name="list"),
    path("<int:pk>/", PauseDetailView.as_view(), name="detail"),
]
