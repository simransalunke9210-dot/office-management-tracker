from rest_framework import serializers
from .models import Label


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label

        fields = [
            "id",
            "workspace",
            "name",
            "color",
            "cards",
            "created_at",
        ]

        read_only_fields = [
            "created_at",
        ]