from django.urls import path
from .views import home, contacto, categorias, art_escolares, art_varios, bolsos_mochilas, lamparas, libretas_cuadernos, login, nosotros, peluches

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('categorias/', categorias, name="categorias"),
    path('art_escolares/', art_escolares, name="articulos escolares"),
    path('art_varios/', art_varios, name="articulos varios"),
    path('bolsos_mochilas/', bolsos_mochilas, name="bolsos y mochilas"),
    path('lamparas/', lamparas, name="lamparas"),
    path('libretas_cuadernos/', libretas_cuadernos, name="libretas y cuadernos"),
    path('login/', login, name="login"),
    path('nosotros/', nosotros, name="nosotros"),
    path('peluches/', peluches, name="peluches"),
]