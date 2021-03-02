import datetime

from django.db import models

# Create your models here.

ESTADO_DEL_PEDIDO = [
    ('E', 'En Proceso'),
    ('M', 'Enviando'),
    ('C', 'Cancelado'),
    ('F', 'Facturado'),
]

class Pedido(models.Model):
    fecha = models.DateTimeField(verbose_name='Fecha', auto_now=False, auto_now_add=True)
    hora_solicitud = models.TimeField(verbose_name='Hora de solicitud')
    hora_entrega = models.TimeField(verbose_name='Hora de entrega')
    descripcion = models.CharField(verbose_name='Descripcion', max_length=250)  #Van los productos seleccionados
    direccion = models.CharField(max_length=250, verbose_name='Direccion')
    mensajero = models.ForeignKey("Mensajero", verbose_name="Mensajero", on_delete=models.DO_NOTHING)
    restaurante = models.ForeignKey("Restaurante", verbose_name="Restaurante", on_delete=models.DO_NOTHING)
    valor = models.IntegerField(verbose_name='Valor')
    tiempo = models.IntegerField(verbose_name='Tiempo aproximado del pedido (min)')
    estado = models.CharField(verbose_name='Estado', max_length=20, choices=ESTADO_DEL_PEDIDO, default='E')

class Mensajero(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=50)
    tfno = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=250, verbose_name='Direccion')
    foto = models.ImageField(verbose_name='foto', upload_to='mensajeros')
    email = models.EmailField(verbose_name='e-mail')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    descripcion = models.CharField(verbose_name='Nombre', max_length=250)
    valor = models.IntegerField(verbose_name='Valor')
    tiempo = models.IntegerField(verbose_name='Tiempo aproximado de preparacion (min)')
    categoria = models.ForeignKey('Categoria', verbose_name='Categoria', on_delete=models.CASCADE)
    restaurante = models.ForeignKey("Restaurante", verbose_name="Restaurante", on_delete=models.CASCADE)
    foto = models.ImageField(verbose_name='Foto', upload_to='productos')

    
class Categoria(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    descripcion = models.CharField(verbose_name='Nombre', max_length=250)
    foto = models.ImageField(verbose_name= 'Foto', upload_to='categoria')
    restaurante = models.ForeignKey("Restaurante", verbose_name="Restaurante", on_delete=models.CASCADE)
    
class Administrador(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=50)
    tfno = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=250, verbose_name='Direccion')
    foto = models.ImageField(verbose_name='Foto', upload_to='administrador')
    email = models.EmailField(verbose_name='e-mail')
    
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=50)
    tfno = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=250, verbose_name='Direccion')
    foto = models.ImageField(verbose_name='Foto', upload_to='usuarios')
    email = models.EmailField(verbose_name='e-mail')
    nombre_usuario = models.CharField(verbose_name='Nombre', max_length=50)
    
    def __str__(self):
        return self.nombre

class Restaurante(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    direccion = models.CharField(max_length=250, verbose_name='Direccion')
    tfno = models.IntegerField(verbose_name='Telefono')
    email = models.EmailField(verbose_name='e-mail')
    logo = models.ImageField(verbose_name= 'Foto', upload_to='restaurantes')

    def __str__(self):
        return self.nombre

#Se almacena un registro diario de las ventas totales y por restaurantes
class Reporte_all(models.Model):
    fecha = models.DateField(verbose_name='Fecha', auto_now_add=True)
    total_vendido = models.DecimalField(decimal_places=2, verbose_name='Venta total del dia', max_digits=2)
    top_ventas_por_restaurantes = models.CharField(verbose_name='Top de Restaurantes por venta', max_length=500)
    categoria_mas_vendida = models.ForeignKey("Categoria", on_delete=models.DO_NOTHING, verbose_name='Categoria mas vendida')

#Se almacena un reporte diario de ventas por restaurante que posteriormente se enviará a cada uno
#   de los que registren ventas ese dia
class Reporte(models.Model):
    fecha = models.DateField(verbose_name='Fecha', auto_now_add=True)
    total_valor_vendido = models.DecimalField(decimal_places=2, verbose_name='Venta total del dia', max_digits=2)
    ventas_por_categoria = models.CharField(max_length=500, verbose_name='Ventas por Categoria')
    
class Valoracion(models.Model):
    fecha = models.DateField(verbose_name='Fecha', auto_now_add=True)
    restaurante = models.ForeignKey("Restaurante", verbose_name="Restaurante", on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='e-mail', null=True, blank=True)
    valoracion = models.DecimalField(verbose_name='valoracion', decimal_places=2, max_digits=2)
    comentario = models.CharField(verbose_name='Reseñas', max_length=2000)
