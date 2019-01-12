from django import forms
from django.forms import TextInput
from .models import Book
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class BookForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'price', 'book_type', 'publication_date')

        widgets = {
            'publication_date': TextInput(attrs={'type': 'date'}),
        }

        error_messages = {
            'title': {
                'required': 'kiritilishi shart',
            },
            'price': {
                'enter': 'togri kirit dabba...'

            },
            'publication_date': {
                'invalid': 'sana xato kiritilgan',
            },
        }







