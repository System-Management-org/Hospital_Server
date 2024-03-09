from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

class MyApiView(APIView):
    # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     # Access the current user
    #     current_user = request.user

    #     # Now you can use the current_user object as needed
    #     user_data = {
    #         'username': current_user.username,
    #         # Add more fields as needed
    #     }
    
    #     return Response(user_data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
