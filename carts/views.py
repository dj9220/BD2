from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Cart, CartItem, Order
from shop.models import Product
# Create your views here.

def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {'cart': cart}
    else:
        empty_message = "Pirkimo krepšelis yra tuščias"
        context = {'empty': True, 'empty_message':empty_message}
    return render(request, 'carts/cart-view.html', context)

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return redirect(reverse('view_cart'))
    cartitem = CartItem.objects.get(id=id)
    cartitem.cart = None
    cartitem.save()
    return redirect(reverse('view_cart'))



def add_to_cart(request, id):
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id']=new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if update_qty and qty:
        if int(qty)==0:
            product.quantity+=cart_item.quantity
            cart_item.delete()

        elif product.quantity<int(qty):
            messages.error(request,f'Neteisingas kiekis')
            cart_item.delete()
            return redirect(reverse('shop:all_products'))
        else:
            cart_item.quantity = qty
            product.quantity -= int(qty)
            product.save()
            cart_item.save()
    else:
        pass


    return redirect(reverse('view_cart'))

def checkout(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return redirect(reverse('view_cart'))
    if request.user.is_authenticated:
        new_order, created = Order.objects.get_or_create(cart=cart, status="Sėkmingas", user=request.user)


    del request.session['cart_id']
    del request.session['items_total']


    return redirect(reverse('view_cart'))

def all_orders(request):
    orders = Order.objects.all().order_by('-timestamp')
    page = request.GET.get('page', 1)

    for i in orders:
        i.total = i.cart.total
        i.save()
    paginator = Paginator(orders, 20)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'carts/All_orders.html', {'orders':orders, 'users':users})