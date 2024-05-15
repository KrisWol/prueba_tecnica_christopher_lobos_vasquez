import csv
import os

from django.core.management.base import BaseCommand
from django.db.models import Sum, Count
from entidades.models import Maestro, Salon

class Command(BaseCommand):
    help = 'Realiza consultas a la base de datos'

    def handle(self, *args, **options):
        # Obtener la suma total de todos los sueldos
        total_sueldo = Maestro.objects.aggregate(Sum('sueldo'))['sueldo__sum']
        print(f"Suma total de sueldos: {total_sueldo}")

        # Obtener la cantidad total de salones que el código sea “COD”
        total_salones_cod = Salon.objects.filter(codigo='COD').count()
        print(f"Total de salones con código 'COD': {total_salones_cod}")

        # Mostrar un listado de maestros y salones ordenados por cantidad de salones
        maestros_salones = Maestro.objects.annotate(num_salones=Count('salon')).order_by('-num_salones')
        for maestro in maestros_salones:
            print(f"{maestro.nombre_completo}: {maestro.num_salones} salones")
