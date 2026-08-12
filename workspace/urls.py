from django.urls import path
from .views import (
    WorkspaceListCreateAPIView,
    WorkspaceRetrieveUpdateDeleteAPIView,
)

urlpatterns = [

    path(
        "",
        WorkspaceListCreateAPIView.as_view(),
        name="workspace-list"
    ),

    path(
        "<int:pk>/",
        WorkspaceRetrieveUpdateDeleteAPIView.as_view(),
        name="workspace-detail"
    ),
]