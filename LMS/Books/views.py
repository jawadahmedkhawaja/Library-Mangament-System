from django.shortcuts import render,redirect, get_object_or_404
from .models import Book,Category, IssueRecord
from accounts.models import MemberProfile
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from datetime import date


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


def return_book(request, isbn):
    fine = 0
    if request.method == 'POST':
        member = get_object_or_404(MemberProfile, user=request.user)
        book = get_object_or_404(Book,isbn=isbn)

        issue = IssueRecord.objects.get(member=member,book=book,is_returned=False)

        if issue:
            today = date.today()
            if today > issue.return_date:
                days_late = (today - issue.return_date).days
                fine = days_late * 10

            issue.is_returned = True
            issue.fine = fine
            issue.save()
            book.available_count += 1
            book.save()

        if request.user.is_admin:
            return redirect('admin_dashboard')
        else:
            return redirect('member_dashboard')

def view_books(request):
    books  = Book.objects.all()
    return render(request,'view_books.html',context={'page':'Books','books':books})

def search_book(request):
    title = request.GET.get('q')
    book = Book.objects.filter(title__icontains=title)

    if request.user.is_admin:
        return render(request,'view_books.html',context={'page':title if book.exists() else 'Not Found','books':book})
    else:
        return render(request,'view_books_m.html',context={'page':'Book Search','books':book})

def issue_book(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        book_isbn= request.POST.get('isbn')
        days = abs(request.POST.get('days')
        )

        
        member = get_object_or_404(MemberProfile, user=request.user)
        book = get_object_or_404(Book,isbn=book_isbn)
        return_date = timezone.now().date() + timedelta(days=days)

        if book.available_count == 0:
            messages.error(request,f'Book with ISBN: {book_isbn} not Found, Try Again!')
            return redirect('view_books')
        
        IssueRecord.objects.create(
                member = member,
                book = book,
                return_date = return_date
        )
        book.available_count -= 1
        book.save()

        messages.info(request,f'''Book with ISBN: {book_isbn} Issued to {member.user.username} Successfully!\n
                    Don't Forget to return it before {return_date}. After that you will be fined.''')
        return redirect('view_books')
    return render(request,'issue_book.html',context={'page':'Issue Book'})


def user_fine_view(request):
    member = get_object_or_404(MemberProfile, user=request.user)
    
    today = date.today()

    active_issues = IssueRecord.objects.filter(member=member, is_returned=False)

    total_fine = 0

    for issue in active_issues:
        if today > issue.return_date:
            days_late = (today - issue.return_date).days
            issue.fine = days_late * 10
            issue.save()
            total_fine += issue.fine

    return render(request, 'user_fine.html', {
        'total_fine': total_fine,
        'issue_records': active_issues
    })

