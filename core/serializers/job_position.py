from rest_framework import serializers
from core.models import JobPosition


class JobPositionSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = JobPosition
        fields = ["id","title", "department","department_name","description","required_skills",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]