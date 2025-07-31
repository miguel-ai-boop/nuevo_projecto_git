# Create your views here.
from rest_framework import viewsets
from .models import Cliente, Venta, VentaDetalles
from .serializers import ClienteSerializer, VentaSerializer, VentaDetallesSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaDetallesViewSet(viewsets.ModelViewSet):
    queryset = VentaDetalles.objects.all()
    serializer_class = VentaDetallesSerializer
