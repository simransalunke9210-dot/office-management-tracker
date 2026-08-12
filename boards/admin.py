from django.contrib import admin
from .models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "workspace",
        "created_at",
    )

    search_fields = (
        "title",
        "workspace__name",
    )

    list_filter = (
        "created_at",
    )
