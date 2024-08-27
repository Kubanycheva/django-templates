from django import forms
from.models import Product

class ProductFilter(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'have', 'image']
