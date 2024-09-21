from django.shortcuts import render
from .models import Menu, MenuCategories

# Create your views here.
def menu(request):
    categories = MenuCategories.objects.all()
    
    categories = [key.menu_category_name for key in categories]
    
    query = request.GET.get("category", "")
    
    if query == "":
        menu_items = Menu.objects.all()
        
        context = {
        'menu_items': menu_items,
        }
        
        return render(request, "menu.html", context)
    
    if query in categories:
        category = MenuCategories.objects.get(menu_category_name = query)
        menu_items = Menu.objects.filter(category_id = category)
        context = {
        'menu_items': menu_items,
        'category' : category
        }
        return render(request, "menu.html", context)
    
    return render(request, "menu.html")