from rest_framework import serializers
from core.models import JobPosition


class JobPositionSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = JobPosition
        fields = [
            "id","title","department","department_name",
            "description","required_skills","created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_required_skills(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("required_skills must be a list.")

        for skill in value:
            if not isinstance(skill, str) or not skill.strip():
                raise serializers.ValidationError(
                    "Each skill must be a non-empty string."
                )

        return value