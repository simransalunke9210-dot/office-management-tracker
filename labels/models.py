from django.db import models
from workspace.models import Workspace
from cards.models import Card


class Label(models.Model):

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="labels"
    )

    name = models.CharField(
        max_length=100
    )

    color = models.CharField(
        max_length=20,
        default="#000000"
    )

    cards = models.ManyToManyField(
        Card,
        related_name="labels",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name