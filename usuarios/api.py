# usuarios/api.py
from rest_framework import viewsets, permissions
from .models import Usuario  # Asegúrate que el modelo exista
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]
