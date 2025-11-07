# catalogo/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count

from django.contrib.auth.forms import UserCreationForm  # <-- IMPORT NECESARIO
from django.contrib.auth import login                   # <-- IMPORT NECESARIO

from .models import Producto, Categoria, Etiqueta
from .forms import ProductoForm, CategoriaForm, EtiquetaForm


def index(request):
    return render(request, "index.html")


# ---------- Productos ----------
@login_required
def lista_productos(request):
    q = request.GET.get("q", "")
    categoria_id = request.GET.get("categoria")
    productos = (
        Producto.objects.all()
        .select_related("categoria")
        .prefetch_related("etiquetas")
    )
    if q:
        productos = productos.filter(
            Q(nombre__icontains=q) | Q(descripcion__icontains=q)
        )
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()
    ctx = {"productos": productos, "categorias": categorias, "q": q, "categoria_id": categoria_id}
    return render(request, "productos/lista.html", ctx)


@login_required
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, "Producto creado correctamente.")
            return redirect("detalle_producto", id=producto.id)
    else:
        form = ProductoForm()
    return render(request, "productos/crear.html", {"form": form})


@login_required
def detalle_producto(request, id):
    producto = get_object_or_404(
        Producto.objects.select_related("categoria"), pk=id
    )
    return render(request, "productos/detalle.html", {"producto": producto})


@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    initial = {
        "dimensiones": getattr(producto.detalle, "dimensiones", ""),
        "peso": getattr(producto.detalle, "peso", None),
    }
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado.")
            return redirect("detalle_producto", id=producto.id)
    else:
        form = ProductoForm(instance=producto, initial=initial)
    return render(request, "productos/editar.html", {"form": form, "producto": producto})


@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == "POST":
        producto.delete()
        messages.info(request, "Producto eliminado.")
        return redirect("lista_productos")
    return render(request, "productos/eliminar.html", {"producto": producto})


# ---------- Categorías ----------
@login_required
def lista_categorias(request):
    cats = Categoria.objects.annotate(n=Count("productos")).all()
    return render(request, "categorias/lista.html", {"categorias": cats})


@login_required
def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creado.")
            return redirect("lista_categorias")
    else:
        form = CategoriaForm()
    return render(request, "categorias/formulario.html", {"form": form})


@login_required
def editar_categoria(request, id):
    obj = get_object_or_404(Categoria, pk=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada.")
            return redirect("lista_categorias")
    else:
        form = CategoriaForm(instance=obj)
    return render(request, "categorias/formulario.html", {"form": form, "obj": obj})


@login_required
def eliminar_categoria(request, id):
    obj = get_object_or_404(Categoria, pk=id)
    if request.method == "POST":
        obj.delete()
        messages.info(request, "Categoría eliminada.")
        return redirect("lista_categorias")
    return render(request, "categorias/eliminar.html", {"obj": obj})


# ---------- Etiquetas ----------
@login_required
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, "etiquetas/lista.html", {"etiquetas": etiquetas})


@login_required
def crear_etiqueta(request):
    if request.method == "POST":
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Etiqueta creada.")
            return redirect("lista_etiquetas")
    else:
        form = EtiquetaForm()
    return render(request, "etiquetas/formulario.html", {"form": form})


@login_required
def editar_etiqueta(request, id):
    obj = get_object_or_404(Etiqueta, pk=id)
    if request.method == "POST":
        form = EtiquetaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Etiqueta actualizada.")
            return redirect("lista_etiquetas")
    else:
        form = EtiquetaForm(instance=obj)
    return render(request, "etiquetas/formulario.html", {"form": form, "obj": obj})


@login_required
def eliminar_etiqueta(request, id):
    obj = get_object_or_404(Etiqueta, pk=id)
    if request.method == "POST":
        obj.delete()
        messages.info(request, "Etiqueta eliminada.")
        return redirect("lista_etiquetas")
    return render(request, "etiquetas/eliminar.html", {"obj": obj})


# ---------- Registro de usuarios ----------
def register(request):
    # Opcional: si ya está autenticado, no mostrar el registro
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login tras registrarse (puedes quitarlo si no lo quieres)
            login(request, user)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})
