from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.models import ScreeningResult
from core.serializers.screening_result import ScreeningResultSerializer


@api_view(["GET"])
def screening_result_detail(request, pk):
    screening_result = get_object_or_404(ScreeningResult, pk=pk)
    serializer = ScreeningResultSerializer(screening_result)

    return Response(
        {
            "success": True,
            "message": "Screening result retrieved successfully.",
            "data": serializer.data
        },
        status=status.HTTP_200_OK
    )