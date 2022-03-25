from django import forms
from ..models.product.mobile_phone.mobile_phone import MobilePhone 

class MobilePhoneForm(forms.ModelForm):
    
    screen = forms.CharField(max_length=20)
    model = forms.CharField(max_length=20)
    ram = forms.CharField(max_length=20)
    brand = forms.CharField(max_length=20)
    rom = forms.CharField(max_length=20)
   
    class Meta:
        model = MobilePhone
        fields = ['screen', 'model', 'ram', 'brand', 'rom']