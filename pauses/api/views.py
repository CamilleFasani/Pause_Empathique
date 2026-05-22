from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from pauses.models import Pause

from .serializers import PauseSerializer


class PauseListCreateView(generics.ListCreateAPIView):
    serializer_class = PauseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Pause.objects.filter(user=self.request.user).prefetch_related(
            "feelings", "needs"
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PauseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PauseSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch", "delete", "head", "options"]

    def get_queryset(self):
        return Pause.objects.filter(user=self.request.user).prefetch_related(
            "feelings", "needs"
        )
