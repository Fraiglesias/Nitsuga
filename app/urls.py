from django.urls import path
from .views import home, contacto, categorias, artescolares, art_varios, bolsos_mochilas, lamparas, libretas_cuadernos, login, nosotros, peluches, gestion_home, gestion_usuarios, gestion_roles, gestion_productos, gestion_categorias

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('categorias/', categorias, name="categorias"),
    path('artescolares/', artescolares, name="artescolares"),
    path('art_varios/', art_varios, name="art_varios"),
    path('bolsos_mochilas/', bolsos_mochilas, name="bolsos_mochilas"),
    path('lamparas/', lamparas, name="lamparas"),
    path('libretas_cuadernos/', libretas_cuadernos, name="libretas_cuadernos"),
    path('login/', login, name="login"),
    path('nosotros/', nosotros, name="nosotros"),
    path('peluches/', peluches, name="peluches"),
    path('gestion/home/', gestion_home, name="gestion_home"),
    path('gestion/usuarios/', gestion_usuarios, name="gestion_usuarios"),
    path('gestion/roles/', gestion_roles, name="gestion_roles"),
    path('gestion/productos/', gestion_productos, name="gestion_productos"),
    path('gestion/categorias/', gestion_categorias, name="gestion_categorias"),
]