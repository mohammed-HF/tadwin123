from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful user creation
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('loggedin')  # Redirect to the logged-in page
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html')

##def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or other URL
        else:
            # Handle invalid login credentials
            return redirect('login')  # Redirect back to the login page with an error message
    else:
        return render(request, 'login.html')## 
    


def loggedin_view(request):
    return render(request, 'loggedin.html')  # Render the logged-in page template





def login_form(request):
    return render(request, 'login_form.html')







