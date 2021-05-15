from django.contrib import admin
from .models import Product, Supplier, Category, SubCategories, Check
# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(SubCategories)
admin.site.register(Check)
admin.site.site_header = 'Administrator'
admin.site.site_title = 'Administrator'
admin.site.index_title = 'Data'
