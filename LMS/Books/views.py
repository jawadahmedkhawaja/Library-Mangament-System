from django.shortcuts import render,redirect, get_object_or_404
from .models import Book,Category
from django.contrib import messages

def add_book(request):
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
            return redirect('add_book')
        
        category_obj, created = Category.objects.get_or_create(name=category)
        Book.objects.create(
                    title = title,
                    author = author,
                    isbn = isbn,
                    quantity = int(quantity),
                    available_count = int(available_count) ,
                    category =  category_obj
        )
        messages.info(request,f'Book "{title}" added Successfully!')
        return redirect('view_books')
    
    return render(request,'add_book.html', context={'page':'Add Book'})

def delete_book(request,isbn):
    book = get_object_or_404(Book, isbn=isbn)
    book.delete()
    messages.success(request,f'Book with ISBN Number: {isbn} is Deleted!')
    return redirect('view_books')

def update_book(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        author = data.get('author')
        quantity = data.get('quantity')
        available_count = data.get('available_count')
        category_name = data.get('category')

        new_isbn = data.get('isbn')
        if new_isbn != book.isbn and Book.objects.filter(isbn=new_isbn).exists():
            messages.error(request, "Another book with this ISBN already exists!")
            return redirect('update_book', isbn=isbn)

        category_obj, _ = Category.objects.get_or_create(name=category_name)

        book.title = title
        book.author = author
        book.isbn = new_isbn
        book.quantity = int(quantity)
        book.available_count = int(available_count) 
        book.category = category_obj
        book.save()

        messages.success(request, f'Book "{title}" updated successfully!')
        return redirect('view_books')

    return render(request, 'update_book.html', context={'page': 'Update Books', 'book': book})


def return_book(request,isbn):
    pass

def view_books(request):
    books  = Book.objects.all()
    return render(request,'view_books.html',context={'page':'Books','books':books})

def search_book(request):
    pass

def issue_book(request,book_name):
    pass