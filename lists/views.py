from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import List
from .serializers import ListSerializer


class ListListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return List.objects.filter(
            board__workspace__owner=self.request.user
        )


class ListRetrieveUpdateDeleteAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return List.objects.filter(
            board__workspace__owner=self.request.user
        )