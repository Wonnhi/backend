from django.shortcuts import render
from. models import Product

def get_product(reguest):
    product = Product.objects.all()
    return render(request, {'product': product})