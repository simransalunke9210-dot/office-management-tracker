from django.db import models
from django.conf import settings
from cards.models import Card


class Comment(models.Model):

    task = models.ForeignKey(
    Card,
    on_delete=models.CASCADE,
    related_name="comments",
    null=True,
    blank=True
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.task.title}"