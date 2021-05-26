from django import forms
from .models import Product, Supplier, Check, ProductInCheck


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price', 'supplier', 'subCategory']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'phone_number', 'email', 'adress']
class SendEmailForm(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)
class CheckForm(forms.ModelForm):
    class Meta:
        model= ProductInCheck
        fields=['product','quantity','price']
class CheckCheckForm(forms.ModelForm):
    class Meta:
        model=Check
        exclude=['price_total',]