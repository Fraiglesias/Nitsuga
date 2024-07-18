from django.contrib import admin
from .models import Marca, Colores, Producto, Categoria, Condicion
# Register your models here.

admin.site.register(Marca)
admin.site.register(Colores)
admin.site.register(Producto)
admin.site.register(Condicion)
admin.site.register(Categoria)
