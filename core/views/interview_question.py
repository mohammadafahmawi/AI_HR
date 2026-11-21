from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.models import InterviewQuestionSet
from core.serializers.interview_question import InterviewQuestionSetSerializer


@api_view(["GET"])
def interview_question_detail(request, pk):
    question_set = get_object_or_404(InterviewQuestionSet, pk=pk)
    serializer = InterviewQuestionSetSerializer(question_set)

    return Response(
        {
            "success": True,
            "message": "Interview question set retrieved successfully.",
            "data": serializer.data
        },
        status=status.HTTP_200_OK
    )