from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from core.serializers.resume import ResumeUploadSerializer


class ResumeUploadAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]  \

    def post(self, request):
        serializer = ResumeUploadSerializer(data=request.data)

        if serializer.is_valid():
            resume = serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Resume uploaded successfully.",
                    "data": ResumeUploadSerializer(resume).data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "success": False,
                "message": "Validation failed.",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )