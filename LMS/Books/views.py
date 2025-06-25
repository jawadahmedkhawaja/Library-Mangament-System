from django.shortcuts import render
from .models import Book

def add_Book(request):
    if request.method == 'POST':
        data = request.POST.get()

def delete_book(request):
    pass

def update_book(request,isbn):
    pass

def return_book(request,isbn):
    pass

def view_books(request):
    pass

def search_book(request):
    pass
