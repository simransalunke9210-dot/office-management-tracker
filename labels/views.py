from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Label
from .serializers import LabelSerializer


class LabelListCreateView(generics.ListCreateAPIView):

    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Label.objects.filter(
            workspace__owner=self.request.user
        ).order_by("name")


class LabelDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Label.objects.filter(
            workspace__owner=self.request.user
        )