from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from workspace.models import Workspace
from boards.models import Board
from lists.models import List
from cards.models import Card


class DashboardAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        # Total workspaces owned by the logged-in user
        workspace_count = Workspace.objects.filter(
            owner=user
        ).count()

        # Total boards inside user's workspaces
        board_count = Board.objects.filter(
            workspace__owner=user
        ).count()

        # Total lists inside user's workspaces
        list_count = List.objects.filter(
            board__workspace__owner=user
        ).count()

        # Total cards/tasks assigned to the logged-in user
        task_count = Card.objects.filter(
            assigned_to=user
        ).count()

        return Response({

            "employee": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
            },

            "summary": {
                "workspaces": workspace_count,
                "boards": board_count,
                "lists": list_count,
                "total_tasks": task_count,
            }
        })