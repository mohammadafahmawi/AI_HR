from django.contrib import admin
from core.models import (
    Candidate,
    Department,
    InterviewQuestionSet,
    JobPosition,
    Resume,
    ScreeningResult,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "department", "created_at")
    list_filter = ("department", "created_at")
    search_fields = ("title", "description")


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "created_at")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("created_at",)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "uploaded_at")
    list_filter = ("uploaded_at",)
    search_fields = ("candidate__full_name", "candidate__email")


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "job_position", "score", "recommendation", "generated_at")
    list_filter = ("recommendation", "generated_at", "job_position")
    search_fields = ("candidate__full_name", "job_position__title", "summary")


@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "job_position", "generated_at")
    list_filter = ("generated_at", "job_position")
    search_fields = ("candidate__full_name", "job_position__title")