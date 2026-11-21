from django.db import models as django_models
from django.core.validators import MinValueValidator, MaxValueValidator


class ScreeningResult(django_models.Model):
    class Recommendation(django_models.TextChoices):
        PROCEED = "proceed", "Proceed"
        HOLD = "hold", "Hold"
        REJECT = "reject", "Reject"

    candidate = django_models.ForeignKey(
        "Candidate",
        on_delete=django_models.CASCADE,
        related_name="screening_results"
    )
    job_position = django_models.ForeignKey(
        "JobPosition",
        on_delete=django_models.CASCADE,
        related_name="screening_results"
    )
    score = django_models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    strengths = django_models.JSONField(default=list)
    missing_skills = django_models.JSONField(default=list)
    recommendation = django_models.CharField(
        max_length=20,
        choices=Recommendation.choices,
        default=Recommendation.HOLD
    )
    summary = django_models.TextField(blank=True, null=True)
    raw_report = django_models.TextField(blank=True, null=True)
    generated_at = django_models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-generated_at"]
        db_table = "screening_results"

    def __str__(self):
        return f"Screening for {self.candidate} - {self.job_position} ({self.score}%)"