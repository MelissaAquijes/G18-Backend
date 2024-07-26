from rest_framework import serializers
from .models import CategoriaModel, ProductoModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    img_url_full = serializers.CharField(source = 'img_url.url', read_only = True)

    def validate_precio(self, precio):
        if precio < 0:
            raise serializers.ValidationError(
                "El precio debe ser mayor a cero")
        return precio

    class Meta:
        model = ProductoModel
        fields = ['id', 'nombre', 'precio', 'descripcion','categoria', 'img_url' ,'img_url_full']

class productGetSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
   
    img_url_full = serializers.CharField(source = 'img_url.url', read_only = True)
    
    class Meta:
        model = ProductoModel

        fields = ['id', 'nombre', 'precio', 'descripcion','categoria', 'img_url','img_url_full']
