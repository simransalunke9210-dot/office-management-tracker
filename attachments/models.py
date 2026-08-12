from django.db import models
from cards.models import Card


class Attachment(models.Model):

    ATTACHMENT_TYPE_CHOICES = (
        ("FILE", "File"),
        ("YOUTUBE", "YouTube"),
    )

    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name="attachments"
    )

    attachment_type = models.CharField(
        max_length=20,
        choices=ATTACHMENT_TYPE_CHOICES
    )

    file = models.FileField(
        upload_to="attachments/",
        blank=True,
        null=True
    )

    youtube_url = models.URLField(
        blank=True,
        null=True
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title or f"Attachment {self.id}"