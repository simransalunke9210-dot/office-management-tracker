from django.urls import path
from .views import (
    CardListCreateAPIView,
    CardRetrieveUpdateDeleteAPIView,
)

urlpatterns = [

    path(
        "",
        CardListCreateAPIView.as_view(),
        name="card-list"
    ),

    path(
        "<int:pk>/",
        CardRetrieveUpdateDeleteAPIView.as_view(),
        name="card-detail"
    ),
]