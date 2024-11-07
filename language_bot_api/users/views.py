"""
Views for users app.
"""
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserCreateSerializer


class UserCreateView(APIView):
    """API view for creating a new user"""

    @swagger_auto_schema(
        operation_description="Create a new user",
        operation_summary="Create a new user",
    )
    def post(self, request):
        """Method POST"""
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "data": serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {"status": False, "data": serializer.data, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
