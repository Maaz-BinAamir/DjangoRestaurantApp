from django.shortcuts import render, redirect
from cart.models import Cart
from django.contrib.auth.models import User

# Create your views here.
def checkout(request):
    
    current_user = request.user
    user = User.objects.get(username=current_user)  
    cart_items = Cart.objects.filter(user = user)
    
    cost = 0
    no_of_items = 0
    
    print("username", user)
    
    for items in cart_items:
        cost += items.cost
        no_of_items += 1
    
    context = {
        'cart_items' : cart_items,
        'cost' : cost,
        'no_of_items' : no_of_items
    }
    
    
    return render(request, "checkout.html", context)

def process_checkout(request):
    
    return render(request, 'order_failed.html')