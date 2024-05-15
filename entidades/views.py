from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Maestro
from .serializers import MaestroSerializer

class MaestroViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        completo = self.request.query_params.get('completo')
        if completo:
            queryset = queryset.prefetch_related('salon_set')
        return queryset
