from django.forms import ModelForm
from django import forms
from .models import Products

class ProductsForm(ModelForm):

    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'preco' : forms.FloatInput(attrs={'class': 'form-control' }),
            'descricao' : forms.TextInput(attrs={'class': 'form-control' }),
            'curso': forms.ImageInput(attrs={'class': 'form-control' })
        }