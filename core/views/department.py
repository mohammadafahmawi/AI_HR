from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.department import DepartmentSerializer


class DepartmentCreateAPIView(APIView):
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)

        if serializer.is_valid():
            department = serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Department created successfully.",
                    "data": DepartmentSerializer(department).data
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