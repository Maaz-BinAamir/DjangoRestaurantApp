from django.shortcuts import render
from django.shortcuts import redirect

def homepage(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contact(request):
    return render(request, "contact.html")
