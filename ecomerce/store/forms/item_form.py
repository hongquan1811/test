from django import forms
from ..models.product.item import Item 

class ItemForm(forms.ModelForm):
    price = forms.FloatField()
    discount = forms.CharField(max_length=4)
    image = forms.ImageField()
   
    class Meta:
        model = Item
        fields = ['price', 'discount', 'image']