from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='restaurant')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='restaurant/logo/%Y/%m/%d/')


    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                related_name='customer')
    avatar = models.ImageField(upload_to='customer/%Y/%m/%d/')
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='driver')
    avatar = models.ImageField(upload_to='driver/%Y/%m/%d/')
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
    
class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                  related_name='meal')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='meal/%Y/%m/%d/')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created',)


class Order(models.Model):
    STATUSES = (
        ('pending','Pending'),
        ('progress', 'Progress'),
        ('ready', 'Ready'),
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                    related_name='order')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, 
                                related_name='order')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                                related_name='order')
    address = models.CharField(max_length=100)
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    picked_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUSES, default='pending')

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        ordering = ('-created',)

class OrderDetail(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE,
                            related_name='order_detail')
    meal = models.ForeignKey("Meal", on_delete=models.CASCADE,
                            related_name='order_detail')
    quantity = models.IntegerField()
    subtotal = models.IntegerField()

    def __str__(self):
        return str(self.id)