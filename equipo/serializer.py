from rest_framework import serializers
from .models import equipo


class equipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = equipo
        fields = ('id', 'nombre', 'descripcion', 'posicion', 'created_at', )
        read_only_fields = ('created_at', )
        

