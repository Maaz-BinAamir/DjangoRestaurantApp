from django.shortcuts import render, redirect
from .models import Cart
from django.contrib.auth.models import User
from menuapp.models import Menu

# Create your views here.
def cart(request):
    
    if not request.user.is_authenticated:
        return render(request, "notloggedin.html")
        
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
    
    
    return render(request, "cart.html", context)

def add_to_cart(request, item_id):
    current_user = request.user
    user = User.objects.get(username=current_user)
    item = Menu.objects.get(id = item_id)
    quantity = int(request.POST.get('quantity', '1'))
    Cart.objects.create(user = user, item = item, quantity = quantity)
    
    return redirect(request.META.get('HTTP_REFERER'))

def delete_cart_item(request, item_id):
    Cart.objects.get(id = item_id).delete()
    
    return redirect('cart')