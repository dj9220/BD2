from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.views.generic import DetailView

from .models import Cart, CartItem, Order
from shop.models import Product
# Create your views here.

