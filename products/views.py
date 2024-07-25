from rest_framework.views import APIView
from .models import CategoriaModel, ProductoModel
from .serializers import CategoriaSerializer, ProductoSerializer, productGetSerializer
from rest_framework.response import Response
from rest_framework import status


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
        #print(request.data)
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            
            img_url = serializer.validated_data['img_url']
            img_url.name = 'images/' + img_url.name
    #agregar imagen = serializer.save()
            imagen = serializer.save()
            
            img_url_full = imagen.img_url.url
            imagen.img_url_full = img_url_full
            imagen.save()

            respuesta = ProductoSerializer(imagen)
            return Response(respuesta.data, status = status.HTTP_201_CREATED)
           
            #serializer.save()
            #return Response({"msg": respuesta.data})
        else:
        
            return Response({"msg": serializer.errors})
        
class ProductDeletePut(APIView):
    def delete(self, request, pk):
        productos = ProductoModel.objects.get(id=pk)
        productos.delete()
        return Response ({"msg:": "eliminacion exitosa"})

    def put(self, request, pk):
        try:
            categoria = CategoriaModel.objects.get(pk=pk)
        except CategoriaModel.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)