from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from commerce_app.models import Stuff

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.user.username} cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"{self.quantity} x {self.item}"
    
    
    def total_price(self):
        return self.quantity * self.item.price
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16, default="-")
    address = models.TextField(max_length=512)
    country = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip_code = models.PositiveIntegerField()

    date_ordered = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.user.username}, {self.email}, {self.first_name}, {self.last_name}, {self.address}, {self.country}, {self.state}, {self.zip_code}"
    
    
    def total_price(self):
        order_items = OrderItem.objects.filter(order=self)
        return sum(item.total_price() for item in order_items)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    
    def __str__(self):
        return f"{self.quantity} x {self.item}"

    
    def total_price(self):
        return self.quantity * self.item.price