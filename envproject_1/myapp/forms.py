# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'Author', 'PulicationDate', 'Price']

    def clean_Price(self):
        price = self.cleaned_data.get('Price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
