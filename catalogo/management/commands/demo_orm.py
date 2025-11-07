from django.core.management.base import BaseCommand
from catalogo.models import Producto, Categoria
from django.db import connection
from django.db.models import Avg, Count, Q

class Command(BaseCommand):
    help = "Demostración de consultas ORM y raw SQL"

    def handle(self, *args, **opts):
        self.stdout.write("1) Productos precio > 50 (filter)")
        for p in Producto.objects.filter(precio__gt=50):
            self.stdout.write(f" - {p}")

        self.stdout.write("\n2) Excluir categoría 'Servicios' (exclude)")
        for p in Producto.objects.exclude(categoria__nombre__iexact="Servicios"):
            self.stdout.write(f" - {p}")

        self.stdout.write("\n3) Búsqueda por nombre o descripción (Q objects)")
        for p in Producto.objects.filter(Q(nombre__icontains="pro") | Q(descripcion__icontains="pro")):
            self.stdout.write(f" - {p}")

        self.stdout.write("\n4) Anotaciones: promedio por categoría")
        cats = Categoria.objects.annotate(avg=Avg("productos__precio"), n=Count("productos"))
        for c in cats:
            self.stdout.write(f" - {c.nombre}: {c.n} prod, avg=${c.avg or 0:.2f}")

        self.stdout.write("\n5) RAW SQL: top 5 más caros")
        with connection.cursor() as cur:
            cur.execute("""SELECT id, nombre, precio FROM catalogo_producto ORDER BY precio DESC LIMIT 5""")
            for row in cur.fetchall():
                self.stdout.write(f" - {row}")
