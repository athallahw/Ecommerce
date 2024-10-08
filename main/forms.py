from django import forms
from main.models import ProductEntry
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = ProductEntry
        fields = ['name', 'price', 'description', 'quantity']
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        name = strip_tags(name)
        if "<script>" in name or "javascript:" in name:
            raise ValidationError("Invalid input detected!")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        description = strip_tags(description)
        if "<script>" in description or "javascript:" in description:
            raise ValidationError("Invalid input detected!")
        return description
