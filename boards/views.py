from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Board
from .serializers import BoardSerializer


class BoardListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(
            workspace__owner=self.request.user
        )


class BoardRetrieveUpdateDeleteAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(
            workspace__owner=self.request.user
        )
