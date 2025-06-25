from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
