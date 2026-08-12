from django.urls import path

from .views import (
    AttachmentListCreateAPIView,
    AttachmentRetrieveUpdateDeleteAPIView,
)


urlpatterns = [

    path(
        "",
        AttachmentListCreateAPIView.as_view(),
        name="attachment-list"
    ),

    path(
        "<int:pk>/",
        AttachmentRetrieveUpdateDeleteAPIView.as_view(),
        name="attachment-detail"
    ),

]