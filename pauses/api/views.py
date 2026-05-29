from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from pauses.models import AnonymousPauseCounter, Pause

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


class IsAnonymousOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class AnonymousCounterView(APIView):
    permission_classes = [IsAnonymousOnly]

    def post(self, request):
        AnonymousPauseCounter.increment()
        return Response(status=status.HTTP_204_NO_CONTENT)
