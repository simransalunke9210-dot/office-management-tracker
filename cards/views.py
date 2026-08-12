from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Card
from .serializers import CardSerializer


class CardListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Card.objects.filter(
            task_list__board__workspace__owner=self.request.user
        )

        # Filter by status
        status_filter = self.request.query_params.get("status")

        if status_filter:
            queryset = queryset.filter(
                status=status_filter
            )

        # Filter by priority
        priority_filter = self.request.query_params.get("priority")

        if priority_filter:
            queryset = queryset.filter(
                priority=priority_filter
            )

        # Filter by assigned employee
        assigned_to_filter = self.request.query_params.get("assigned_to")

        if assigned_to_filter:
            queryset = queryset.filter(
                assigned_to_id=assigned_to_filter
            )

        # Filter by due date
        due_date_filter = self.request.query_params.get("due_date")

        if due_date_filter:
            queryset = queryset.filter(
                due_date=due_date_filter
            )

        # Search by task title
        search = self.request.query_params.get("search")

        if search:
            queryset = queryset.filter(
                title__icontains=search
            )

        return queryset


class CardRetrieveUpdateDeleteAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Card.objects.filter(
            task_list__board__workspace__owner=self.request.user
        )