from rest_framework import serializers
from .models import Cliente, Venta, VentaDetalles

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

    def validate_cliente(self, value):
        if not Cliente.objects.filter(pk=value.id).exists():
            raise serializers.ValidationError("El cliente no existe.")
        return value

class VentaDetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaDetalles
        fields = '__all__'

    def validate_producto(self, value):
        if value is None:
            raise serializers.ValidationError("El producto es obligatorio.")
        return value

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor a 0.")
        return value

    def validate(self, data):
        if 'venta' not in data:
            raise serializers.ValidationError({"venta": "La venta es obligatoria."})
        return data
