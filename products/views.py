from rest_framework.views import APIView
from .models import CategoriaModel, ProductoModel
from .serializers import CategoriaSerializer, ProductoSerializer, productGetSerializer
from rest_framework.response import Response

class CategoriaListCreate(APIView):
    def get(self, request):
        caterogia = CategoriaModel.objects.all()
        serializer = CategoriaSerializer(caterogia, many=True)
        return Response({"msg": serializer.data }) 
        
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": serializer.data})
        else:
            return Response({"msg": "datos incorrectos"})
        
class CategoriaDelete(APIView):
    def delete(self, request, pk):
        categoria = CategoriaModel.objects.get(id=pk)
        categoria.delete()
        return Response ({"msg:": "eliminacion exitosa"})
        
class ProductListCreate(APIView):
    def get(self, request):
        productos= ProductoModel.objects.all()
        serializer = productGetSerializer(productos, many=True)
        return Response(serializer.data)
    
    ##################################################################
    def post(self, request): 
        print(request.data)
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({"msg": serializer.data})
        else:
        #serializer.errors
            return Response({"msg": serializer.errors})
    
class ProductDelete(APIView):
    def delete(self, request, pk):
        productos = ProductoModel.objects.get(id=pk)
        productos.delete()
        return Response ({"msg:": "eliminacion exitosa"})
