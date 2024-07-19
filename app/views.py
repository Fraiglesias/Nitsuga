from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Producto, Categoria, Pedido, DetallePedido, Marca, Colores, Condicion
from .forms import ProductoForm, CategoriaForm, MarcaForm, ColoresForm, CondicionForm
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
    pedidos = Pedido.objects.all()
    data = {
        'pedidos' : pedidos
    }
    return render(request, 'app/gestion/home.html', data)

def gestion_usuarios(request):
    return render(request, 'app/gestion/usuarios.html')

def gestion_roles(request):
    return render(request, 'app/gestion/roles.html')

def gestion_productos(request):
    return render(request, 'app/gestion/productos.html')

def gestion_categorias(request):
    return render(request, 'app/gestion/categorias.html')

def detalle_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    productos = Producto.objects.filter(categoria=id)
    data = {
        'categoria': categoria,
        'producto' : productos
    }

    return render(request, 'app/categorias.html', data)

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


def crear_categoria(request):

    data = { 
        'form': CategoriaForm()
    }    

    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "Categoria creada correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/categorias/crear.html', data)  

def listar_categoria(request):

    categorias = Categoria.objects.all()

    data = {
        'categorias' : categorias
    }

    return render(request, 'app/categorias/listar.html', data)

def editar_categoria(request, id):

    categorias = get_object_or_404(Categoria, id=id)

    data = {
        'form': CategoriaForm(instance=categorias)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=categorias)
        if formulario.is_valid:
            formulario.save()
            return redirect('app:listar_categorias')
        else:
            data["form"] = formulario

    return render(request, 'app/categorias/editar.html', data)  

def eliminar_categoria(request, id):

    categorias = get_object_or_404(Categoria, id=id)
    categorias.delete()
    return redirect('app:listar_categoria')

def crear_marca(request):

    data = { 
        'form': MarcaForm()
    }    

    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "Marca creada correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/marcas/crear.html', data)  

def listar_marca(request):

    marcas = Marca.objects.all()

    data = {
        'marcas' : marcas
    }

    return render(request, 'app/marcas/listar.html', data)

def editar_marca(request, id):

    marcas = get_object_or_404(Marca, id=id)

    data = {
        'form': MarcaForm(instance=marcas)
    }

    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=marcas)
        if formulario.is_valid:
            formulario.save()
            return redirect('app:listar_marca')
        else:
            data["form"] = formulario

    return render(request, 'app/marcas/editar.html', data)  

def eliminar_marca(request, id):

    marcas = get_object_or_404(Marca, id=id)
    marcas.delete()
    return redirect('app:listar_marca')

def crear_color(request):

    data = { 
        'form': ColoresForm()
    }    

    if request.method == 'POST':
        formulario = ColoresForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "Color creado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/colores/crear.html', data)  

def listar_color(request):

    colores = Colores.objects.all()

    data = {
        'colores' : colores
    }

    return render(request, 'app/colores/listar.html', data)

def editar_color(request, id):

    colores = get_object_or_404(Colores, id=id)

    data = {
        'form': ColoresForm(instance=colores)
    }

    if request.method == 'POST':
        formulario = ColoresForm(data=request.POST, instance=colores)
        if formulario.is_valid:
            formulario.save()
            return redirect('app:listar_color')
        else:
            data["form"] = formulario

    return render(request, 'app/colores/editar.html', data)  

def eliminar_color(request, id):

    colores = get_object_or_404(Colores, id=id)
    colores.delete()
    return redirect('app:listar_color')

def crear_condicion(request):

    data = { 
        'form': CondicionForm()
    }    

    if request.method == 'POST':
        formulario = CondicionForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "Condicion creada correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/condicion/crear.html', data)  

def listar_condicion(request):

    condicion = Condicion.objects.all()

    data = {
        'condicion' : condicion
    }

    return render(request, 'app/condicion/listar.html', data)

def editar_condicion(request, id):

    condicion = get_object_or_404(Condicion, id=id)

    data = {
        'form': CondicionForm(instance=condicion)
    }

    if request.method == 'POST':
        formulario = CondicionForm(data=request.POST, instance=condicion)
        if formulario.is_valid:
            formulario.save()
            return redirect('app:listar_condicion')
        else:
            data["form"] = formulario

    return render(request, 'app/condicion/editar.html', data)  

def eliminar_condicion(request, id):

    condicion = get_object_or_404(Condicion, id=id)
    condicion.delete()
    return redirect('app:listar_condicion')

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
            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=1
            )

    return JsonResponse({'status': 1})