from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora_solicitud', 'hora_entrega', 'descripcion', 
        'direccion', 'mensajero', 'restaurante', 'valor', 'tiempo', 'estado')

@admin.register(models.Mensajero)
class MensajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'tfno', 'direccion', 'foto')

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'valor', 'tiempo', 'categoria')

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'foto', 'restaurante')

@admin.register(models.Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'tfno', 'direccion', 'foto', 'email')

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'tfno', 'direccion', 'foto', 'email', 'nombre_usuario')

@admin.register(models.Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'tfno', 'email', 'logo')

@admin.register(models.Reporte_all)
class ReporteAllAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'total_vendido', 'top_ventas_por_restaurantes', 'categoria_mas_vendida')

@admin.register(models.Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'total_valor_vendido', 'ventas_por_categoria')

@admin.register(models.Valoracion)
class ValoracionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'restaurante', 'email', 'valoracion', 'comentario')