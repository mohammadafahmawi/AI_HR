from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.serializers.department import DepartmentSerializer


@api_view(["POST"])
def department_create(request):
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