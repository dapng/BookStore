from django.db import models
from .models import Books
from django.forms import ModelForm, fields, widgets, TextInput, NumberInput, Textarea, URLInput, BooleanField


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'description', 'price', 'quantity', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги'
            }),
            "image": URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на обложку'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор книги'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание книги'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость книги'
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество книг'
            }),
        }


class SaleBook(ModelForm):
    class Meta:
        sale = BooleanField(required=True)
        model = Books
        fields = ['sale', 'quantity_sale']

        widgets = {
            "quantity_sale": NumberInput(attrs={
                'class': 'form-control',
                'style': 'width:239px; margin:auto',
                'placeholder': 'Количество книг на продажу'
            }),
        }