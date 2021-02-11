from django.db import models
from django.contrib.auth.models import User # Importo los usuarios para poder relacionarla con la clase Post y que cada vez que un usuario se de de baja, sus post se borren

# Create your models here.
# Hay que crear una clase de cada elemento del Blog que querramos completar

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta: # 
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre
        
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True) # Indica que no es obligatorio incluir una imagen
    autor=models.ForeignKey(User, on_delete=models.CASCADE) # Indica que elimine los posts de los usuarios que se vayan
    categorias=models.ManyToManyField(Categoria) # Indica que un Post puede tener varias categorias y una Categoria puede estar en varios Posts
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta: # 
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo
        
