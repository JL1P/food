from . import models
from rest_framework import serializers

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pedido
        fields = '__all__'

class MensajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mensajero
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Producto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrador
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurante
        fields = '__all__'

class ReporteAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reporte_all
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reporte
        fields = '__all__'

class ValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Valoracion
        fields = '__all__'
