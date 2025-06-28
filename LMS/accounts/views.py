from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Books.models import Book, IssueRecord
from django.db.models import Sum
from .models import MemberProfile


def add_member(request):
    pass


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)

        if user:
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")

            if user.is_admin: # type: ignore
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html',context={'page': 'Login'})

def logout_page(request):
    logout(request)
    return redirect('login')


def admin_dashboard(request):
    total_books = Book.objects.aggregate(total=Sum('quantity'))['total'] or 0
    available_books = Book.objects.aggregate(available=Sum('available_count'))['available'] or 0
    fine_collected = IssueRecord.objects.filter(is_returned=True).aggregate(total=Sum('fine'))['total'] or 0
    fine_remaining = IssueRecord.objects.filter(is_returned=False).aggregate(total=Sum('fine'))['total'] or 0

    return render(request,'admin_dashboard.html',
                  context={'page':'Admin',
                           'total_books': total_books,
                           'available_books': available_books,
                           'fine_collected': fine_collected,
                            'fine_remaining': fine_remaining,
                            'user':request.user.username})

def member_dashboard(request):
    member = get_object_or_404(MemberProfile,user=request.user)
    books_borrowed = Book.objects.filter(member=member)
    return render(request,'member_dashboard.html',context={'page':f'{request.user}','books':books_borrowed})
