from django import forms
from main.models import ProductEntry

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = ProductEntry
        fields = ['name', 'price', 'description', 'quantity']
