from django import forms
from ..models.product.laptop.laptop import Laptop 

class LaptopForm(forms.ModelForm):
    
    ram = forms.CharField(max_length=20)
    rom = forms.CharField(max_length=20)
    cpu = forms.CharField(max_length=20)
    screen = forms.CharField(max_length=500)
    model = forms.CharField(max_length=20)
   
    class Meta:
        model = Laptop
        fields = ['ram', 'rom', 'cpu', 'screen', 'model']