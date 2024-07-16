from django.urls import path
from .views import CategoriaListCreate

urlpatterns = [
    path ("categorias/", CategoriaListCreate.as_view())
]