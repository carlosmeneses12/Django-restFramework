from equipo.models import equipo
from rest_framework import viewsets, permissions
from .serializer import equipoSerializer

class equipoViewSet(viewsets.ModelViewSet):
    queryset = equipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = equipoSerializer