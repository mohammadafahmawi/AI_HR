from rest_framework import serializers
from core.models import InterviewQuestionSet


class InterviewQuestionSetSerializer(serializers.ModelSerializer):
    job_position_title = serializers.CharField(source="job_position.title", read_only=True)

    class Meta:
        model = InterviewQuestionSet
        fields = ["id","job_position","job_position_title","questions","created_at",
        ]