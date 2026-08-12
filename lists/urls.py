from django.urls import path
from .views import (
    ListListCreateAPIView,
    ListRetrieveUpdateDeleteAPIView,
)

urlpatterns = [

    path(
        "",
        ListListCreateAPIView.as_view(),
        name="list-list"
    ),

    path(
        "<int:pk>/",
        ListRetrieveUpdateDeleteAPIView.as_view(),
        name="list-detail"
    ),
]