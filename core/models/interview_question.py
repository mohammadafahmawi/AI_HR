from django.db import models as django_models


class InterviewQuestionSet(django_models.Model):
    candidate = django_models.ForeignKey(
        "Candidate",
        on_delete=django_models.CASCADE,
        related_name="interview_questions"
    )
    job_position = django_models.ForeignKey(
        "JobPosition",
        on_delete=django_models.CASCADE,
        related_name="interview_questions"
    )
    screening_result = django_models.ForeignKey(
        "ScreeningResult",
        on_delete=django_models.CASCADE,
        related_name="interview_questions"
    )
    technical_questions = django_models.JSONField(default=list)
    behavioral_questions = django_models.JSONField(default=list)
    follow_up_questions = django_models.JSONField(default=list)
    generated_at = django_models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-generated_at"]
        db_table = "interview_question_sets"

    def __str__(self):
        return f"Questions for {self.candidate} - {self.job_position}"