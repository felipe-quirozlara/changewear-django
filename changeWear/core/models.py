from django.contrib.admin.sites import site
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.base import Model

# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return str(self.usuario.username)

class Producto(models.Model):

    MUJER = 'MJ'
    HOMBRE = 'HM'
    NINO = 'NN'

    CATEGORIA_PRODUCTO = [
        (MUJER, 'Mujer'),
        (HOMBRE, 'Hombre'),
        (NINO, 'Niño'),
    ]

    titulo = models.CharField(max_length=30)
    precio = models.CharField(max_length=10)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_PRODUCTO)
    descripcion = models.TextField(null=False)
    imagen = models.ImageField()

    def __str__(self):
        return str(self.titulo + ' ' + self.categoria)

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False, null=True, blank=False)
    transaccion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str('Nro.Compra: '+str(self.id)+ ' - Cliente: ' + self.cliente.usuario.username)

    @property
    def get_comprar_total(self):
        try:
            productos = self.productocompra_set.all()
            total = sum([item.get_total for item in productos])
        except:
            total = None
        return total

    @property
    def get_comprar_productos(self):
        try:
            productos = self.productocompra_set.all()
            total = sum([item.cantidad for item in productos])
        except:
            total = 0
        return total

    @property
    def get_productos(self):
        try:
            productos = self.productocompra_set.all()
            nombre = [item.ret_nombre for item in productos]
        except:
            nombre = 'Sin producto'
        return nombre

class ProductoCompra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str('Nro.Compra: '+str(self.compra.id) + ' - Producto: ' +self.producto.titulo)

    # Metodos para la suma
    @property
    def get_total(self):
        try:
            total = int(self.producto.precio) * self.cantidad
        except:
            total = 0
        return total

    @property
    def ret_nombre(self):
        try: 
            return self.producto.titulo
        except:
            return 'Sin producto'

class DireccionEnvio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    comuna = models.CharField(max_length=200, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False, null=True, blank=False)
    
    
    def __str__(self):
        return str('Cliente: '+self.cliente.usuario.username + '- Dirección: ' + self.direccion)

class Contactanos(models.Model):
    
    correo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return str(self.correo)

class DataEmpleo(models.Model):
    correo = models.CharField(max_length=50)
    nombrecompleto = models.CharField(max_length=100)
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return str(self.dataempleo.name)
