from django.urls import path
from .views import home, contacto, categorias, art_escolares, art_varios, bolsos_mochilas, lamparas, libretas_cuadernos, login, nosotros, peluches, gestion_home, gestion_usuarios, gestion_roles, gestion_productos, gestion_categorias, valida_login, detalle_categoria, crear_producto, listar_producto, editar_producto, eliminar_producto, crear_categoria, listar_categoria, editar_categoria, crear_pedido, eliminar_categoria, crear_marca, editar_marca, listar_marca, eliminar_marca, crear_color, listar_color, editar_color, eliminar_color, crear_condicion, listar_condicion, editar_condicion, eliminar_condicion

app_name = 'app'

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('categorias/', categorias, name="categorias"),
    path('categorias/1/', art_escolares, name="art_escolares"),
    path('categorias/2/', art_varios, name="art_varios"),
    path('categorias/4/', bolsos_mochilas, name="bolsos_mochilas"),
    path('categorias/7/', lamparas, name="lamparas"),
    path('categorias/5/', libretas_cuadernos, name="libretas_cuadernos"),
    path('login/', login, name="login"),
    path('nosotros/', nosotros, name="nosotros"),
    path('categorias/6/', peluches, name="peluches"),
    
    path('gestion/home/', gestion_home, name="gestion_home"),
    path('gestion/usuarios/', gestion_usuarios, name="gestion_usuarios"),
    path('gestion/roles/', gestion_roles, name="gestion_roles"),
    path('gestion/productos/', gestion_productos, name="gestion_productos"),
    path('gestion/categorias/', gestion_categorias, name="gestion_categorias"),
    path('categorias/<id>/', detalle_categoria, name='detalle_categoria'),
    path('valida_login/', valida_login, name='valida_login'),
    path('crear_producto/', crear_producto, name="crear_producto"),
    path('listar_producto/', listar_producto, name="listar_producto"),
    path('editar_producto/<id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('crear_categoria/', crear_categoria, name="crear_categoria"),
    path('listar_categoria/', listar_categoria, name="listar_categoria"),
    path('editar_categoria/<id>/', editar_categoria, name='editar_categoria'),
    path('eliminar_categoria/<id>/', eliminar_categoria, name='eliminar_categoria'),
    path('crear_marca/', crear_marca, name="crear_marca"),
    path('listar_marca/', listar_marca, name="listar_marca"),
    path('editar_marca/<id>/', editar_marca, name='editar_marca'),
    path('eliminar_marca/<id>/', eliminar_marca, name='eliminar_marca'),
    path('crear_color/', crear_color, name="crear_color"),
    path('listar_color/', listar_color, name="listar_color"),
    path('editar_color/<id>/', editar_color, name='editar_color'),
    path('eliminar_color/<id>/', eliminar_color, name='eliminar_color'),
    path('crear_condicion/', crear_condicion, name="crear_condicion"),
    path('listar_condicion/', listar_condicion, name="listar_condicion"),
    path('editar_condicion/<id>/', editar_condicion, name='editar_condicion'),
    path('eliminar_condicion/<id>/', eliminar_condicion, name='eliminar_condicion'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    
]