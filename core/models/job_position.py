from django.db import models as django_models


class JobPosition(django_models.Model):
    department = django_models.ForeignKey(
        "core.Department",
        on_delete=django_models.CASCADE,
        related_name="job_positions"
    )
    title = django_models.CharField(max_length=150)
    description = django_models.TextField(blank=True, null=True)
    required_skills = django_models.JSONField(default=list)
    created_at = django_models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]
        db_table = "job_positions"

    def __str__(self):
        return self.title