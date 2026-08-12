from django.contrib import admin
from .models import Attachment


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "card",
        "attachment_type",
        "created_at",
    )

    search_fields = (
        "title",
        "card__title",
    )

    list_filter = (
        "attachment_type",
        "created_at",
    )