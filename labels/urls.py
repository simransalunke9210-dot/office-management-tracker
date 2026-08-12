from django.urls import path
from .views import (
    LabelListCreateView,
    LabelDetailView
)


urlpatterns = [

    path(
        '',
        LabelListCreateView.as_view(),
        name="label-list"
    ),

    path(
        '<int:pk>/',
        LabelDetailView.as_view(),
        name="label-detail"
    ),

]