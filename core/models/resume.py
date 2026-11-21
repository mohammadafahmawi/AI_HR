from django.db import models as django_models


class Resume(django_models.Model):
    candidate = django_models.ForeignKey(
        "Candidate",
        on_delete=django_models.CASCADE,
        related_name="resumes"
    )
    file = django_models.FileField(upload_to="resumes/")
    uploaded_at = django_models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]
        db_table = "resumes"

    def __str__(self):
        return f"Resume - {self.candidate}"