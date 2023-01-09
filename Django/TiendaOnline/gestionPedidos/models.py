from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=9, verbose_name='celular')

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField()
    
    def __str__(self) -> str:
        return 'El numero es %s, la fecha es %s y el estado de la entrega es: %s' %(self.numero, self.fecha, self.estado)