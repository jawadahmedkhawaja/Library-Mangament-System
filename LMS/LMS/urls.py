from django.contrib import admin
from django.urls import path
from accounts.views import login_page, logout_page
from Books.views import add_book, return_book, issue_book, delete_book, update_book, view_books, search_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),
    path('add-book/',add_book,name='add_book'),
    path('return-book/',return_book,name='return_book'),
    path('issue-book/<isbn>/',issue_book,name='issue_book'),
    path('delete-book/<isbn>/', delete_book, name='delete_book'),
    path('update-book/<isbn>/',update_book,name='update_book'),
    path('view-books/',view_books,name='view_books'),
    path('search-books/',search_book,name='search_book'),
    
]
