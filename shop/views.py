from django.shortcuts import render
from .models import *

def shop(request):
    chocolates = Chocolate.objects.all()
    context = {'chocolates' :chocolates}
    return render(request, 'shop/shop.html', context)

def basket(request):
    context = {}
    return render(request, 'shop/basket.html', context)

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)