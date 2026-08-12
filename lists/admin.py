from django.contrib import admin
from .models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "board",
        "position",
    )

    search_fields = (
        "title",
        "board__title",
    )

    list_filter = (
        "board",
    )
