
# Create your models here.
from django.db import models

class Maestro(models.Model):
    nombre_completo = models.CharField(max_length=100, default="nombre default")
    sueldo = models.FloatField(default=1000)

    def __str__(self):
        return self.nombre_completo

class Salon(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    letra = models.CharField(max_length=100, default="A")
    maestro = models.ForeignKey(Maestro, on_delete=models.SET_NULL, null=True, blank=True, related_name="salones")

    def __str__(self):
        return self.codigo
