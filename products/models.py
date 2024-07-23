from django.db import models

class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)

class ProductoModel(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.TextField()
    precio = models.FloatField(blank=False, null=False)
    categoriaId = models.ForeignKey(
        CategoriaModel, related_name='productos', 
        on_delete=models.CASCADE ),
    img_url = models.ImageField(upload_to='images/', blank = True, null=True)
    img_url_full = models.URLField(blank = True, null=True)
