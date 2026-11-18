from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.candidate import CandidateSerializer


class CandidateCreateAPIView(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)

        if serializer.is_valid():
            candidate = serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Candidate registered successfully.",
                    "data": CandidateSerializer(candidate).data
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