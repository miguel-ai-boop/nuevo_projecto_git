# ventas/api.py
from rest_framework import viewsets, permissions
from .models import Venta  # Asegúrate que el modelo exista
from .serializers import VentaSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.AllowAny]
