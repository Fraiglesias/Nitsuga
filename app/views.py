from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Producto, Categoria
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

def valida_login(request):
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list("name", flat=True)
        if "Administrador" in user_groups:
            return redirect('gestion_home')
        elif "Cliente" in user_groups:
            return redirect('home')
        else:
            return redirect('login')