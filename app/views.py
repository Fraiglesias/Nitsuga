from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages

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

def valida_login(request):
    if request.user.is_authenticated:
        user_groups = request.user.groups.values_list("name", flat=True)
        if "Administrador" in user_groups:
            return redirect('gestion_home')
        elif "Cliente" in user_groups:
            return redirect('home')
        else:
            return redirect('login')

def valida_login_old(request):

    if request.method == 'POST': 
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')

        # Validar si el usuario existe
        try:
            usuario = User.objects.get(email=correo)
        except User.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
            return redirect('contacto')

        # Autenticar al usuario
        usuario = authenticate(request, username=usuario.username, password=contrasenia)
        if usuario is not None: # Verificar si el usuario pertenece al grupo 'administrador'
            if usuario.groups.filter(name='Administrador').exists():
                login(usuario) # Redirigir a la página de gestion después de iniciar sesión
                return redirect('gestion/home') 
            else:
                login(usuario)
                return redirect('home/')
        else:
            messages.error(request, 'Contraseña incorrecta.')
            return redirect('login/')
    else:
        return render(request, 'home/')
    
#@login_required 

#def gestion_home(request):
    # Vista protegida para usuarios administradores
   # return render(request, 'gestion/home.html')