from django.contrib import admin
from .models import Marca, Colores, Producto, Usuario, Categoria 
# Register your models here.

admin.site.register(Marca)
admin.site.register(Colores)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Categoria)
