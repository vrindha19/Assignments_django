# books/urls.py
from django.urls import path
from .views import book_list, add_book

app_name = 'books'

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/add/', add_book, name='add_book'),
    # Add other URL patterns as needed
]
