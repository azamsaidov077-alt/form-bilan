from django import forms
from .models import *


class CategoryForm(forms.Form):
    category_name = forms.CharField(
        max_length=100,
        label="Kategoriya nomi",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Kategoriya nomini kiriting'
        })
    )
    description = forms.CharField(
        required=False,
        label="Tavsif",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Tavsif kiriting',
            'rows': 4
        })
    )
    image = forms.ImageField(
        required=False,
        label="Rasm",
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )


class ProductsForm(forms.Form):
    product_name = forms.CharField(
        max_length=100,
        label="Mahsulot nomi",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mahsulot nomini kiriting'
        })
    )
    category_id = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Kategoriya",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    unit_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Narxi",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0.00',
            'step': '0.01'
        })
    )
    discounted = forms.BooleanField(
        required=False,
        initial=False,
        label="Chegirmali",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    image = forms.ImageField(
        required=False,
        label="Rasm",
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )


class SuppliersForm(forms.Form):
    company_name = forms.CharField(
        max_length=100,
        label="Kompaniya nomi",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Kompaniya nomini kiriting'
        })
    )
    contact_name = forms.CharField(
        max_length=100,
        label="Kontakt shaxs",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Kontakt shaxs nomini kiriting'
        })
    )
    address = forms.CharField(
        max_length=100,
        label="Manzil",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Manzilni kiriting'
        })
    )
    city = forms.CharField(
        max_length=100,
        label="Shahar",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Shaharni kiriting'
        })
    )


class OrdersForm(forms.Form):
    customer_name = forms.CharField(
        required=False,
        max_length=100,
        label="Mijoz ismi",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mijoz ismini kiriting'
        })
    )
    order_date = forms.DateField(
        label="Buyurtma sanasi",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    required_date = forms.DateField(
        label="Kerakli sana",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    shipped_date = forms.DateField(
        required=False,
        label="Yuborilgan sana",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )