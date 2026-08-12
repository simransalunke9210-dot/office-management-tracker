from django.urls import path
from .views import (
    BoardListCreateAPIView,
    BoardRetrieveUpdateDeleteAPIView,
)

urlpatterns = [

    path(
        "",
        BoardListCreateAPIView.as_view(),
        name="board-list"
    ),

    path(
        "<int:pk>/",
        BoardRetrieveUpdateDeleteAPIView.as_view(),
        name="board-detail"
    ),
]