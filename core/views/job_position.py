from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.job_position import JobPositionSerializer


class JobPositionCreateAPIView(APIView):
    def post(self, request):
        serializer = JobPositionSerializer(data=request.data)

        if serializer.is_valid():
            job_position = serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Job position created successfully.",
                    "data": JobPositionSerializer(job_position).data
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