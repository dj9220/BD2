from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shop import models as shop_model
from users.models import Message
from carts.models import Order
@login_required(login_url='login')
def dashboard(request):
    all_products = shop_model.Product.objects.filter(quantity__lte=10)
    total_product = shop_model.Product.objects.count()
    total_suppliers = shop_model.Supplier.objects.count()
    total_categories = shop_model.Category.objects.count()
    total_subCategories = Message.objects.count()
    all_orders = Order.objects.count()
    context = {
        'products':all_products,
        'product':total_product,
        'supplier':total_suppliers,
        'categories':total_categories,
        'message':total_subCategories,
        'orders':all_orders,
            }
    return render(request, 'users/dashboard.html', context)