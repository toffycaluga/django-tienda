from django import forms
from .models import Producto, Categoria, Etiqueta, DetalleProducto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ["nombre"]

class ProductoForm(forms.ModelForm):
    # campos del OneToOne incluidos en el mismo form
    dimensiones = forms.CharField(required=False)
    peso = forms.DecimalField(required=False, max_digits=6, decimal_places=2)

    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "categoria", "etiquetas", "dimensiones", "peso"]
        widgets = {
            "etiquetas": forms.CheckboxSelectMultiple,
        }

    def save(self, commit=True):
        producto = super().save(commit)
        # crear/actualizar detalle
        det, _ = DetalleProducto.objects.get_or_create(producto=producto)
        det.dimensiones = self.cleaned_data.get("dimensiones") or ""
        det.peso = self.cleaned_data.get("peso")
        det.save()
        return producto
