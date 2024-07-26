from django.urls import path
from .views import CategoriaListCreate, ProductListCreate, CategoriaDelete, ProductDeletePut

urlpatterns = [
    path ("categorias/", CategoriaListCreate.as_view()),
    path ("productos/", ProductListCreate.as_view()), #name='subida_img'
    path("categorias/<int:pk>", CategoriaDelete.as_view()),
    path("productos/<int:pk>", ProductDeletePut.as_view()),
]