from rest_framework import serializers
from .models import Categoria, Producto

# Serializador para Categoría
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ('created_at',)

# Serializador para Producto
class ProductoSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category', read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'name', 'description', 'price', 'category', 'category_name']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser un valor positivo.")
        return value

    def validate_category(self, value):
        if not Categoria.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La categoría no existe.")
        return value
