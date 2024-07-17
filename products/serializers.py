from rest_framework import serializers
from .models import CategoriaModel, ProductoModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoriaId = CategoriaSerializer()
   
    class Meta:
        model = ProductoModel

        fields = ['id', 'nombre', 'precio', 'descripcion','categoriaId']


