"""
URL configuration for Nitsuga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('app.urls')),
    path('', views.home, name="home"),
    
    path('contacto/', views.contacto, name="contacto"),
    path('categorias/', include('app.urls')),
    path('categorias/', views.categorias, name="categorias"),
    path('art_escolares/', views.art_escolares, name="art_escolares"),
    path('art_varios/', views.art_varios, name="art_varios"),
    path('bolsos_mochilas/', views.bolsos_mochilas, name="bolsos_mochilas"),
    path('lamparas/', views.lamparas, name="lamparas"),
    path('libretas_cuadernos/', views.libretas_cuadernos, name="libretas_cuadernos"),
    path('login/', views.login, name="login"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('peluches/', views.peluches, name="peluches"),
 
    path('gestion/home/', views.gestion_home, name='gestion_home'),
    path('gestion/usuarios/', views.gestion_usuarios, name="gestion_usuarios"),
    path('gestion/roles/', views.gestion_roles, name="gestion_roles"),
    path('gestion/productos/', views.gestion_productos, name="gestion_productos"),
    path('gestion/categorias/', views.gestion_categorias, name="gestion_categorias"),


    path('accounts/', include('django.contrib.auth.urls')), 
    # path('accounts/logout/', include('django.contrib.auth.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)