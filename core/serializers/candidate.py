from rest_framework import serializers
from core.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "job_position", "first_name", "last_name", "email", "phone", "applied_at"]
        read_only_fields = ["id", "applied_at"]