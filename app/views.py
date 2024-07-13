from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def categorias(request):
    return render(request, 'app/categorias.html')

def artescolares(request):
    return render(request, 'app/artescolares.html')

def art_varios(request):
    return render(request, 'app/art_varios.html')

def bolsos_mochilas(request):
    return render(request, 'app/bolsos_mochilas.html')

def lamparas(request):
    return render(request, 'app/lamparas.html')

def libretas_cuadernos(request):
    return render(request, 'app/libretas_cuadernos.html')

def login(request):
    return render(request, 'app/login.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def peluches(request):
    return render(request, 'app/peluches.html')

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
