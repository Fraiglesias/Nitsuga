from django import forms
from .models import Producto, Categoria, Marca, Colores, Condicion

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'

class ColoresForm(forms.ModelForm):

    class Meta:
        model = Colores
        fields = '__all__'

class CondicionForm(forms.ModelForm):

    class Meta:
        model = Condicion
        fields = '__all__'