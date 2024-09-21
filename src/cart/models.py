from django.db import models
from django.contrib.auth.models import User
from menuapp.models import Menu

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    @property
    def cost(self):
        return self.item.cost * self.quantity
    
    def __str__(self) -> str:
        return str(self.user) + str(self.item) + str(self.quantity)