from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import DepartmentCreateAPIView, JobPositionCreateAPIView, CandidateCreateAPIView, \
    ScreeningResultDetailAPIView, InterviewQuestionSetDetailAPIView
from core.views.resume import ResumeUploadAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/interview-questions/<int:pk>/", InterviewQuestionSetDetailAPIView.as_view(), name="interview-question-detail"),
    path("api/screening-results/<int:pk>/", ScreeningResultDetailAPIView.as_view(), name="screening-result-detail"),
    path("api/resumes/upload/", ResumeUploadAPIView.as_view(), name="resume-upload"),
    path("api/departments/create/", DepartmentCreateAPIView.as_view(), name="department-create"),
    path("api/candidates/create/", CandidateCreateAPIView.as_view(), name="candidate-create"),
    path("api/job-positions/create/", JobPositionCreateAPIView.as_view(), name="job-position-create"),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
