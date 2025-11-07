from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="productos")
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name="productos")

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]
        indexes = [
            models.Index(fields=["nombre"]),
            models.Index(fields=["precio"]),
        ]

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class DetalleProducto(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name="detalle")
    dimensiones = models.CharField(max_length=100, blank=True)   # ej: 10x20x5cm
    peso = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # kg

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"
