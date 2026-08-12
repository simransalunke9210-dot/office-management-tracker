from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):

    labels = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Card
        fields = [
            "id",
            "status",
            "title",
            "description",
            "priority",
            "due_date",
            "position",
            "created_at",
            "updated_at",
            "task_list",
            "assigned_to",
            "labels",
        ]