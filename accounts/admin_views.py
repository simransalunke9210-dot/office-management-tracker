from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import User
from .permissions import IsAdminUserRole

from workspace.models import Workspace
from boards.models import Board
from lists.models import List
from cards.models import Card


class AdminEmployeeListAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request):

        employees = User.objects.filter(
            role=User.EMPLOYEE
        ).order_by("-created_at")

        data = []

        for employee in employees:

            data.append({
                "id": employee.id,
                "username": employee.username,
                "email": employee.email,
                "role": employee.role,
                "profile_picture": (
                    employee.profile_picture.url
                    if employee.profile_picture
                    else None
                ),
                "created_at": employee.created_at,
            })

        return Response(
            {
                "count": len(data),
                "employees": data
            },
            status=status.HTTP_200_OK
        )


class AdminEmployeeTrackerAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminUserRole,
    ]

    def get(self, request, employee_id):

        # -----------------------------------
        # 1. Find employee
        # -----------------------------------

        try:
            employee = User.objects.get(
                id=employee_id,
                role=User.EMPLOYEE
            )

        except User.DoesNotExist:

            return Response(
                {
                    "detail": "Employee not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # -----------------------------------
        # 2. Get employee's workspaces
        # -----------------------------------

        workspaces = Workspace.objects.filter(
            owner=employee
        ).order_by("-created_at")

        workspace_data = []

        for workspace in workspaces:

            # -----------------------------------
            # 3. Get boards inside workspace
            # -----------------------------------

            boards = Board.objects.filter(
                workspace=workspace
            ).order_by("-created_at")

            board_data = []

            for board in boards:

                # -----------------------------------
                # 4. Get lists inside board
                # -----------------------------------

                task_lists = List.objects.filter(
                    board=board
                ).order_by("position")

                list_data = []

                for task_list in task_lists:

                    # -----------------------------------
                    # 5. Get cards inside list
                    # -----------------------------------

                    cards = Card.objects.filter(
                        task_list=task_list
                    ).order_by("position")

                    card_data = []

                    for card in cards:

                        card_data.append({
                            "id": card.id,
                            "title": card.title,
                            "description": card.description,
                            "priority": card.priority,
                            "due_date": card.due_date,
                            "position": card.position,

                            "assigned_to": (
                                {
                                    "id": card.assigned_to.id,
                                    "username": card.assigned_to.username,
                                }
                                if card.assigned_to
                                else None
                            ),

                            "created_at": card.created_at,
                            "updated_at": card.updated_at,
                        })

                    list_data.append({
                        "id": task_list.id,
                        "title": task_list.title,
                        "position": task_list.position,
                        "cards": card_data,
                    })

                board_data.append({
                    "id": board.id,
                    "title": board.title,
                    "description": board.description,
                    "lists": list_data,
                })

            workspace_data.append({
                "id": workspace.id,
                "name": workspace.name,
                "description": workspace.description,
                "boards": board_data,
            })

        # -----------------------------------
        # 6. Return complete tracker
        # -----------------------------------

        return Response(
            {
                "employee": {
                    "id": employee.id,
                    "username": employee.username,
                    "email": employee.email,
                    "role": employee.role,
                },

                "workspaces": workspace_data,
            },

            status=status.HTTP_200_OK
        )
