# config/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from catalogo import views as catalogo  # 👈 importamos las vistas del app

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home
    path("", catalogo.index, name="index"),

    # Auth
    path("login/",  auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # requiere POST
    path("register/", catalogo.register, name="register"),

    # Productos
    path("productos/", catalogo.lista_productos, name="lista_productos"),
    path("productos/crear/", catalogo.crear_producto, name="crear_producto"),
    path("productos/<int:id>/", catalogo.detalle_producto, name="detalle_producto"),
    path("productos/<int:id>/editar/", catalogo.editar_producto, name="editar_producto"),
    path("productos/<int:id>/eliminar/", catalogo.eliminar_producto, name="eliminar_producto"),

    # Categorías
    path("categorias/", catalogo.lista_categorias, name="lista_categorias"),
    path("categorias/crear/", catalogo.crear_categoria, name="crear_categoria"),
    path("categorias/<int:id>/editar/", catalogo.editar_categoria, name="editar_categoria"),
    path("categorias/<int:id>/eliminar/", catalogo.eliminar_categoria, name="eliminar_categoria"),

    # Etiquetas
    path("etiquetas/", catalogo.lista_etiquetas, name="lista_etiquetas"),
    path("etiquetas/crear/", catalogo.crear_etiqueta, name="crear_etiqueta"),
    path("etiquetas/<int:id>/editar/", catalogo.editar_etiqueta, name="editar_etiqueta"),
    path("etiquetas/<int:id>/eliminar/", catalogo.eliminar_etiqueta, name="eliminar_etiqueta"),
]
