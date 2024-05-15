from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Maestro, Salon

class MaestroTests(APITestCase):
    def test_crear_maestro(self):
        url = reverse('maestro-list')
        data = {
            "nombre_completo": "luis rodriguez",
            "sueldo": 2500,
            "salones": [
                {"codigo": "CAV", "letra": "A"},
                {"codigo": "CAB", "letra": "B"},
                {"codigo": "CAC", "letra": "C"},
                {"codigo": "CAD", "letra": "D"},
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('No se permiten más de 3 salones por maestro.', response.data['salones'])

    def test_actualizar_maestro(self):
        maestro = Maestro.objects.create(nombre_completo="luis rodriguez", sueldo=2500)
        Salon.objects.create(codigo="CAV", letra="A", maestro=maestro)
        Salon.objects.create(codigo="CAB", letra="B", maestro=maestro)
        Salon.objects.create(codigo="CAC", letra="C", maestro=maestro)

        url = reverse('maestro-detail', args=[maestro.id])
        data = {
            "nombre_completo": "luis rodriguez",
            "sueldo": 3000,
            "salones": [
                {"codigo": "CAV", "letra": "A"},
                {"codigo": "CAB", "letra": "B"},
                {"codigo": "CAC", "letra": "C"},
                {"codigo": "CAD", "letra": "D"},
            ]
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('No se permiten más de 3 salones por maestro.', response.data['salones'])
