from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


    def __unicode__(self):
        return "Cart id: %s" %(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    line_total = models.DecimalField(default=0.00, decimal_places=2, max_digits=1000)

    def __unicode__(self):
            return self.product.name
STATUS_CHOICES = (
    ('Pradėtas', 'Pradėtas'),
    ('Nutrauktas', 'Nutrauktas'),
    ('Sėkmingas', 'Sėkmingas')
)
class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Pradėtas')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    def __str__(self):
        return str(self.timestamp)