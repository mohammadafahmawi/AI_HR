from rest_framework import serializers
from core.models import ScreeningResult


class ScreeningResultSerializer(serializers.ModelSerializer):
    candidate_name = serializers.CharField(source="candidate.first_name", read_only=True)

    class Meta:
        model = ScreeningResult
        fields = ["id","candidate","candidate_name","score","feedback","status","created_at",
        ]