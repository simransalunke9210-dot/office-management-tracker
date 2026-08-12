from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Attachment
from .serializers import AttachmentSerializer


class AttachmentListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Attachment.objects.filter(
            card__task_list__board__workspace__owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save()


class AttachmentRetrieveUpdateDeleteAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Attachment.objects.filter(
            card__task_list__board__workspace__owner=self.request.user
        )