from rest_framework import serializers
from .models import CategoriaModel, ProductoModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    #categoriaId = CategoriaSerializer()

    img_url_full = serializers.CharField(source = 'img_url.url', read_only = True)

    class Meta:
        model = ProductoModel
        fields = ['id', 'nombre', 'precio', 'descripcion','categoriaId', 'img_url_full']

class productGetSerializer(serializers.ModelSerializer):
    categoriaId = CategoriaSerializer()
   
    img_url_full = serializers.CharField(source = 'img_url.url', read_only = True)
    
    class Meta:
        model = ProductoModel

        fields = ['id', 'nombre', 'precio', 'descripcion','categoriaId', 'img_url_full']

