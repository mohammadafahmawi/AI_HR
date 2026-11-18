from django.db import models as django_models

class Department(django_models.Model):
    name = django_models.CharField(max_length=100, unique=True)
    description = django_models.TextField(blank=True, null=True)
    created_at = django_models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'department'
        ordering = ['name']

    def __str__(self):
        return str(self.name)
