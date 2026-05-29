from django.urls import path

from .views import AnonymousCounterView, PauseDetailView, PauseListCreateView

app_name = "pauses"

urlpatterns = [
    path("", PauseListCreateView.as_view(), name="list"),
    path("anonymous/", AnonymousCounterView.as_view(), name="anonymous"),
    path("<int:pk>/", PauseDetailView.as_view(), name="detail"),
]
