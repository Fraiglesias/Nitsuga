from django.urls import path
from .views import home, contacto, categorias, art_escolares, art_varios, bolsos_mochilas, lamparas, libretas_cuadernos, login, nosotros, peluches, gestion_home, gestion_usuarios, gestion_roles, gestion_productos, gestion_categorias, valida_login, detalle_categoria, crear_producto, listar_producto, editar_producto, eliminar_producto, crear_pedido

app_name = 'app'

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('categoria/', categorias, name="categorias"),
    path('art_escolares/', art_escolares, name="art_escolares"),
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
    path('categoria/<id>/', detalle_categoria, name='detalle_categoria'),
    path('valida_login/', valida_login, name='valida_login'),
    path('crear_producto/', crear_producto, name="crear_producto"),
    path('listar_producto/', listar_producto, name="listar_producto"),
    path('editar_producto/<id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
]