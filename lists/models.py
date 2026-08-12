from django.db import models
from boards.models import Board


class List(models.Model):

    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="lists"
    )

    title = models.CharField(max_length=200)

    position = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.title
