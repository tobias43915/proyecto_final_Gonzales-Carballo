from django.db import models

# Create your models here.

#servicios que ofrecemos

class Servicios(models.Model):
    nombre = models.CharField(max_length=128)
    tiempo=models.CharField(max_length=128)
    valor = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}"

# nombre de las tecnologias

class Tecnologias(models.Model):
   nombre = models.CharField(max_length=128)
   version = models.CharField(max_length=128)
   
   def __str__ (self):
      return f"{self.nombre}"

#nombre de contactos
class Contactos(models.Model):
   nombre = models.CharField(max_length=128)
   apellido = models.CharField(max_length=128)
   email = models.EmailField()
   
   #Se usa para ver la info de SQL en admin

   def __str__(self):
      return f"{self.apellido}, {self.nombre}"