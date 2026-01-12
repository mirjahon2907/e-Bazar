from django import forms
from .models import Product
from django.forms.widgets import FileInput

class MultipleFileInput(FileInput):
    allow_multiple_selected = True


class NewProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'title', 'description', 'price',
            'address', 'category', 'phone_number', 'tg_username',
        )


    def save(self, request, commit=True):
        product = super().save(commit=False)
        product.author = request.user
        if commit:
            product.save()
        return product
    
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'title', 'description', 'price',
            'address', 'category', 'phone_number', 'tg_username',
        )


