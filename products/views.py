from rest_framework.views import APIView
from .models import CategoriaModel
from .serializers import CategoriaSerializer
from rest_framework.response import Response

class CategoriaListCreate(APIView):
    def get(self, request):
        
        producto = CategoriaModel.objects.all()
        serializer = CategoriaSerializer(producto, many=True)
        return Response({"msg": serializer.data }) 
        