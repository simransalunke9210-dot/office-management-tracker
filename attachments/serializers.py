from rest_framework import serializers
from .models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment

        fields = [
            "id",
            "card",
            "attachment_type",
            "file",
            "youtube_url",
            "title",
            "created_at",
        ]

        read_only_fields = [
            "created_at",
        ]

    def validate(self, data):

        attachment_type = data.get("attachment_type")

        file = data.get("file")

        youtube_url = data.get("youtube_url")

        if attachment_type == "FILE":

            if not file:
                raise serializers.ValidationError({
                    "file": "File is required for FILE attachment."
                })

            if youtube_url:
                raise serializers.ValidationError({
                    "youtube_url":
                    "YouTube URL should not be provided for FILE attachment."
                })

        elif attachment_type == "YOUTUBE":

            if not youtube_url:
                raise serializers.ValidationError({
                    "youtube_url":
                    "YouTube URL is required for YOUTUBE attachment."
                })

            if file:
                raise serializers.ValidationError({
                    "file":
                    "File should not be provided for YOUTUBE attachment."
                })

            youtube_url_lower = youtube_url.lower()

            if (
                "youtube.com/" not in youtube_url_lower
                and "youtu.be/" not in youtube_url_lower
            ):
                raise serializers.ValidationError({
                    "youtube_url":
                    "Please provide a valid YouTube URL."
                })

        else:

            raise serializers.ValidationError({
                "attachment_type":
                "Attachment type must be FILE or YOUTUBE."
            })

        return data