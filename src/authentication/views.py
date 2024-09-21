from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from django.contrib.auth import authenticate, login

# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return render(request, 'loggedin.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "login.html")

def signuppage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('signup')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

def logoutview(request):
    logout(request)
    return redirect("home")