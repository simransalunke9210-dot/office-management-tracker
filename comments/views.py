from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Comment
from .serializers import CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(
            task__task_list__board__workspace__owner=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class CommentDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Comment.objects.filter(
            task__task_list__board__workspace__owner=self.request.user,
            user=self.request.user
        )