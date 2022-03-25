from django import forms
from ..models.product.category import Category
from ..models.product.supplier import Supplier
from ..models.product.product import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'supplier'] 