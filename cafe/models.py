from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cafe(models.Model):
    tipo = models.CharField(max_length=64)
    cantidad = models.IntegerField()
    descripcion = models.TextField(null=True)
    precio = models.IntegerField(null=True)
    fecha_entrega = models.DateField(null=True)

    def __str__(self):
        return f"{self.tipo}, {self.cantidad}"

    
class Capsulas(models.Model):
    tipo = models.CharField(max_length=64)
    cantidad = models.IntegerField()
    descripcion = models.TextField(null=True)
    precio = models.IntegerField(null=True)
    fecha_entrega = models.DateField(null=True)

    def __str__(self):
        return f"{self.tipo}, {self.cantidad}"
    
class Te(models.Model):
    tipo = models.CharField(max_length=64)
    cantidad= models.IntegerField()
    fecha_entrega = models.DateField(null=False)
    descripcion = models.TextField(null=True)
    precio = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.tipo}, {self.cantidad}"
    

class Avatar(models.Model):
    # Va a estar asociado con el User. Avatar es una tabla anexa de User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # upload_to es la subcarpeta dentro de la carpeta media
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    DNI = models.IntegerField()
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.DNI}"
    
    
class Acerca(models.Model):
    titulo = models.CharField(max_length=64)
    fecha_entrega = models.DateField(null=False)
    descripcion = models.TextField(null=True)
    link = models.FileField(null=True)

    def __str__(self):
        return f"{self.titulo}, {self.link}"