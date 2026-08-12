from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "assigned_to",
        "priority",
        "due_date",
    )

    search_fields = (
        "title",
        "assigned_to__username",
    )

    list_filter = (
        "priority",
    )