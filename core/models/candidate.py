from django.db import models as django_models


class Candidate(django_models.Model):
    full_name = django_models.CharField(max_length=150)
    email = django_models.EmailField(unique=True)
    phone = django_models.CharField(max_length=20, blank=True, null=True)
    created_at = django_models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "candidates"

    def __str__(self):
        return self.full_name