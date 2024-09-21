from django.db import models

# Create your models here.

class MenuCategories(models.Model):
    menu_category_name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.menu_category_name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    category_id = models.ForeignKey(MenuCategories, on_delete=models.PROTECT, default=None, related_name="category_name")
    
    def __str__(self) -> str:
        return self.name
    
