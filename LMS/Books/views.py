from django.shortcuts import render,redirect
from .models import Book,Category
from django.contrib import messages

def add_Book(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        author = data.get('author')
        isbn = data.get('isbn')
        quantity = data.get('quantity')
        available_count = data.get('quantity')
        category = data.get('category')

        if Book.objects.filter(isbn=isbn).exists():
            messages.error(request, "Book Already Exists!")
            return redirect('/')
        
        category_ = Category.objects.create(name=category)
        Book.objects.create(
                    title = title,
                    author = author,
                    isbn = isbn,
                    quantity = quantity,
                    available_count = available_count ,
                    category =  category_
        )
        messages.info(request,f'Book "{title}" added Successfully!')
        return redirect('/')
    
    return render(request,'add_book.html')

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
