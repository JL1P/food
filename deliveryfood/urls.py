from rest_framework import routers
from . import viewsets

router = routers.SimpleRouter()

router.register('pedido', viewsets.PedidoViewSet)
router.register('mensajero', viewsets.MensajeroViewSet)
router.register('producto', viewsets.ProductoViewSet)
router.register('categoria', viewsets.CategoriaViewSet)
router.register('administrador', viewsets.AdministradorViewSet)
router.register('usuario', viewsets.UsuarioViewSet)
router.register('restaurante', viewsets.RestauranteViewSet)
router.register('reporte_all', viewsets.ReporteAllViewSet)
router.register('reporte', viewsets.ReporteViewSet)
router.register('valoracion', viewsets.ValoracionViewSet)

urlpatterns = router.urls