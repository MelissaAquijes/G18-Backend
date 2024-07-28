from django.contrib import admin
from .models import CategoriaModel, ProductoModel

@admin.register(CategoriaModel)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(ProductoModel)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'categoria')
    search_fields = ('nombre', 'categoria__nombre')
    list_filter = ('categoria',)
    exclude = ('img_url_full',)