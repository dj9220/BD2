from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db.models import Sum
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class SubCategories(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    subCategory = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("shop:all_products")
    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset

class ProductInCheck(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MaxValueValidator(200),MinValueValidator(0)])
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0.00)])

    def __str__(self):
        return self.product.name
    def save(self, *args, **kwargs):
        self.product.quantity +=self.quantity
        self.product.save()
        super(ProductInCheck,self).save(*args,**kwargs)

class Check(models.Model):
    products = models.ManyToManyField(ProductInCheck)
    price_total = models.DecimalField(decimal_places=2, null=True, max_digits=10, validators=[MinValueValidator(0.00)])


