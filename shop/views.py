from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from . import models as models
from django.http import JsonResponse
from django.template import loader
from . import forms as form
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .serializers import ProductSerializer
import json
import csv, io
from django.contrib import messages
import pandas as pd
# Create your views here.

class IndexClassView(ListView):
    model = models.Category
    template_name = 'shop/index.html'
    context_object_name = 'category_list'

class ProductsClassView(ListView):
    model = models.Product
    template_name = 'shop/Product.html'
    context_object_name = 'product_list'


class SupplierClassView(ListView):
    model = models.Supplier
    template_name = 'shop/Supplier.html'
    context_object_name = 'supplier_list'


def subcategoriesList(request,id):
    category = models.SubCategories.objects.filter(category_id=id)
    context= {'category':category}
    return render(request,'shop/Subcategories.html',context)
def products_by_subcategory(request, id):
    product = models.Product.objects.filter(subCategory_id=id)
    return render(request, 'shop/productSubcategory.html',{'products':product})
@login_required(login_url='users:login')
def editProduct(request,id):
    product = models.Product.objects.get(id=id)
    productForm = form.ProductForm(request.POST or None, instance=product)
    if productForm.is_valid():
        productForm.save()
        messages.success(request, f'Produktas sėkmingai pakeistas')
        return redirect('shop:all_products')
    return render(request,'shop/Product form.html',{'form':productForm, 'product':product})

@login_required
def create_product(request):
    form1 = form.ProductForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        messages.success(request, f'Produktas sėkmingai sukurtas')
        return redirect('shop:all_products')
    return render(request, 'shop/Product form.html', {'form':form1})

@login_required(login_url='users:login')
def delete_product(request,id):
    product = models.Product.objects.get(id=id)
    if request.method=='POST':
        product.delete()
        messages.success(request, f'Produktas sėkmingai panaikintas')
        return redirect('shop:all_products')
    return render(request,'shop/delete-product.html', {'product':product})

def search_product(request):
    if request.method == 'POST':
        query_name = request.POST.get('name', None)
        if query_name:
            results = models.Product.objects.filter(name__icontains=query_name)
            return render(request, 'shop/product-search.html', {'results':results})
        return render(request,'shop/product-search.html')

@login_required(login_url='users:login')
def create_supplier(request):
    forms = form.SupplierForm()
    if request.method == 'POST':
        forms = form.SupplierForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,f'Tiekėjas sėkmingai sukurtas')
            return redirect('shop:suppliers')
    return render(request,'shop/SupplierForm.html',{'form':forms})
@login_required
def SendMail(request, id):
    supp = models.Supplier.objects.get(id=id)
    if request.method=='GET':
        forms=form.SendEmailForm()
    else:
        forms =form.SendEmailForm(request.POST)
        if forms.is_valid():
            fromemail = supp.email
            subject = forms.cleaned_data['subject']
            message = forms.cleaned_data['message']
            send_mail(subject,message,fromemail,[supp.email,fromemail])
            messages.success(request,f'Laiškas sėkmingai išsiųstas')
            return redirect('shop:suppliers')
    return render(request,'shop/Email-page.html', {'form':forms})

@login_required
def edit_productQuantity(request, id):
   if request.is_ajax() and request.method == 'POST':
       product = get_object_or_404(models.Product, pk = id)
       product.quantity+=1
       product.save()
       return HttpResponse(product.quantity)
   else:
       return redirect('shop:all_products')

@login_required
def product_in_catalog(request, id):
    product = models.Product.objects.get(id=id)
    return render(request, 'shop/product_in_catalog.html.html', {'product':product})

@login_required
def create_check(request):
    forms = form.CheckForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('shop:all_products')
    return render(request,'shop/CheckForm.html',{'form':forms})

@login_required
def import_csv(request):
    file = pd.read_csv('checks/shop/check1.csv', delimiter=',')
    products = []
    for i in range(len(file)):
        products.append(models.Check(
            product=file.iloc[i][0]
        ))