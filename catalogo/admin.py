from django.contrib import admin
from .models import Categoria, Etiqueta, Producto, DetalleProducto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

class DetalleInline(admin.StackedInline):
    model = DetalleProducto
    can_delete = False
    extra = 0

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "categoria")
    list_filter = ("categoria", "etiquetas")
    search_fields = ("nombre", "descripcion")
    inlines = [DetalleInline]
