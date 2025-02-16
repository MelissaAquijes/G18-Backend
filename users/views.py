from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class userRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # validar los datos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors)
