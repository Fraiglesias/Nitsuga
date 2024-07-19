from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Producto, Categoria, Pedido, DetallePedido
from .forms import ProductoForm
import json
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def categorias(request):
    categoria = Categoria.objects.all()
    data = {
        'categorias' : categoria
    }
    return render(request, 'app/categorias.html', data)

def art_escolares(request):
    productos = Producto.objects.filter(categoria=1)
    data = {
        'productos' : productos
    }
    return render(request, 'app/art_escolares.html', data)

def art_varios(request):
    productos = Producto.objects.filter(categoria=2)
    data = {
        'productos' : productos
    }
    return render(request, 'app/art_varios.html', data)

def bolsos_mochilas(request):
    productos = Producto.objects.filter(categoria=4)
    data = {
        'productos' : productos
    }
    return render(request, 'app/bolsos_mochilas.html', data)

def lamparas(request):
    productos = Producto.objects.filter(categoria=7)
    data = {
        'productos' : productos
    }
    return render(request, 'app/lamparas.html', data)

def libretas_cuadernos(request):
    productos = Producto.objects.filter(categoria=5)
    data = {
        'productos' : productos
    }
    return render(request, 'app/libretas_cuadernos.html', data)

def peluches(request):
    productos = Producto.objects.filter(categoria=6)
    data = {
        'productos' : productos
    }
    return render(request, 'app/peluches.html', data)

def login(request):
    return render(request, 'app/login.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def gestion_home(request):
    return render(request, 'app/gestion/home.html')

def gestion_usuarios(request):
    return render(request, 'app/gestion/usuarios.html')

def gestion_roles(request):
    return render(request, 'app/gestion/roles.html')

def gestion_productos(request):
    return render(request, 'app/gestion/productos.html')

def gestion_categorias(request):
    return render(request, 'app/gestion/categorias.html')

def detalle_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'app/detalle_categoria.html', {'categoria': categoria})

def valida_login(request):
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list("name", flat=True)
        if "Administrador" in user_groups:
            return redirect('gestion_home')
        elif "Cliente" in user_groups:
            return redirect('home')
        else:
            return redirect('login')
        
def crear_producto(request):

    data = { 
        'form': ProductoForm()
    }    

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "Producto creado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/crear.html', data)

def listar_producto(request):

    productos = Producto.objects.all()

    data = {
        'productos' : productos
    }

    return render(request, 'app/producto/listar.html', data)    

def editar_producto(request, id):

    productos = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=productos)
        if formulario.is_valid:
            formulario.save()
            return redirect('app:listar_producto')
        else:
            data["form"] = formulario

    return render(request, 'app/producto/editar.html', data)

def eliminar_producto(request, id):

    productos = get_object_or_404(Producto, id=id)
    productos.delete()
    return redirect('app:listar_producto')

def crear_pedido(request):
    if request.method == 'POST':
        productos_ids = json.loads(request.POST['productos_ids'])
        productos_precio_total = request.POST['productos_precio_total']
        cliente_id = request.POST['cliente_id']

        usuario = User.objects.get(id=cliente_id)

        from datetime import datetime

        pedido = Pedido.objects.create(
            cliente=usuario,
            total=productos_precio_total,
            fecha=datetime.now()
        )

        for producto_id in productos_ids:
            producto = Producto.objects.get(id=producto_id)
            detalle_pedido = DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=1
            )

    return JsonResponse({'status': 1})