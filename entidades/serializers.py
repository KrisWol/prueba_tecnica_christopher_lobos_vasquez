from rest_framework import serializers
from .models import Maestro, Salon

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = [ 'letra','codigo','maestro']

class MaestroSerializer(serializers.ModelSerializer):
    salones = SalonSerializer(many=True, required=False)

    class Meta:
        model = Maestro
        fields = ['id', 'nombre_completo', 'sueldo', 'salones']

    def validate_salones(self, value):
        if len(value) > 3:
            raise serializers.ValidationError("No se permiten más de 3 salones por maestro.")
        return value

    def create(self, validated_data):
        salones_data = validated_data.pop('salones', [])
        maestro = Maestro.objects.create(**validated_data)
        for salon_data in salones_data:
            Salon.objects.create(maestro=maestro, **salon_data)
        return maestro

    def update(self, instance, validated_data):
        salones_data = validated_data.pop('salones', [])
        instance.nombre_completo = validated_data.get('nombre_completo', instance.nombre_completo)
        instance.sueldo = validated_data.get('sueldo', instance.sueldo)
        instance.save()

        for salon_data in salones_data:
            Salon.objects.update_or_create(maestro=instance, codigo=salon_data['codigo'], defaults=salon_data)
        
        return instance
