from django.db import models
from django.conf import settings

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Colores(models.Model):
    nombre = models.CharField(max_length=50)
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Condicion(models.Model):
    nombre = models.CharField(max_length=40)
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, default="None", on_delete=models.PROTECT)
    colores = models.ForeignKey(Colores, default="None", on_delete=models.PROTECT)
    disponible = models.BooleanField()
    condicion = models.ForeignKey(Condicion, default="None", on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, default="None", on_delete=models.PROTECT)


    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    fecha = models.DateTimeField()
    total = models.IntegerField()

    def __str__(self):
        return self.cliente.username

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, default="None", on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, default="None", on_delete=models.PROTECT)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.pedido.cliente.username