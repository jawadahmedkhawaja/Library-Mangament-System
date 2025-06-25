from django.contrib import admin
from django.urls import path
from accounts.views import login_page, logout_page
from Books.views import add_Book, return_book, issue_book, delete_book, update_book, view_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),
    path('add-book/',add_Book,name='add_book'),
    path('return-book/',return_book,name='return_book'),
    path('issue-book/',issue_book,name='issue_book'),
    path('delete-book/', delete_book, name='delete_book'),
    path('update-book/',update_book,name='update_book'),
    path('view-books/',view_books,name='view_books'),
    
]
