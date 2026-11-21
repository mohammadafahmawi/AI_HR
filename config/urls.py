from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import \
    candidate_create, job_position_create, \
    screening_result_detail, interview_question_detail
from core.views.department import department_create
from core.views.resume import  resume_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/interview-questions/<int:pk>/", interview_question_detail, name="interview-question-detail"),
    path("api/screening-results/<int:pk>/", screening_result_detail, name="screening-result-detail"),
    path("api/resumes/upload/", resume_upload, name="resume-upload"),
    path("api/candidates/create/", candidate_create, name="candidate-create"),
    path("api/departments/create/", department_create, name="department-create"),
    path("api/job-positions/create/", job_position_create, name="job-position-create"),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
