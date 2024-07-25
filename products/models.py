from django.db import models

class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class ProductoModel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    img_url = models.ImageField(upload_to='images/', blank=True, null=True) 
    img_url_full = models.URLField(blank=True, null=True)
    categoria = models.ForeignKey(CategoriaModel, related_name='productos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
