from rest_framework import serializers
from core.models import Resume
import os


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "candidate", "file", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]

    def validate_file(self, value):
        ext = os.path.splitext(value.name)[1].lower()
        valid_extensions = ['.pdf', '.docx', '.txt']

        if ext not in valid_extensions:
            raise serializers.ValidationError(
                "Unsupported file format. Only PDF, DOCX, and TXT files are accepted."
            )
        return value