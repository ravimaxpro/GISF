from django import forms
from django.forms import ModelForm
from.models import Product1

class MyProductModelForm(ModelForm):
    title = forms.CharField(required=False, label='Product Title :', widget=forms.TextInput(
                                 attrs={"width": "25 %", "placeholder": "Title of the product"}))
    description=forms.CharField(required=False)
    price=forms.DecimalField

    class Meta:
        model = Product1
        fields = ['title', 'description', 'price']

