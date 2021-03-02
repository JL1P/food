from rest_framework import viewsets
from . import models
from . import serializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = models.Pedido.objects.all()
    serializer_class = serializer.PedidoSerializer

class MensajeroViewSet(viewsets.ModelViewSet):
    queryset = models.Mensajero.objects.all()
    serializer_class = serializer.MensajeroSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = serializer.ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializer.CategoriaSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = models.Administrador.objects.all()
    serializer_class = serializer.AdministradorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializer.UsuarioSerializer

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = models.Restaurante.objects.all()
    serializer_class = serializer.RestauranteSerializer

class ReporteAllViewSet(viewsets.ModelViewSet):
    queryset = models.Reporte_all.objects.all()
    serializer_class = serializer.ReporteAllSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = models.Reporte.objects.all()
    serializer_class = serializer.ReporteSerializer

class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = models.Valoracion.objects.all()
    serializer_class = serializer.ValoracionSerializer