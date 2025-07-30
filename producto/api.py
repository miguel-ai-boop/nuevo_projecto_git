# producto/api.py
from rest_framework import viewsets, filters, permissions
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permissions_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']
