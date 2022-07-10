from django.shortcuts import render

from .models import Category, Chocolate

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_chocolates(request):
    chocolates = Chocolate.objects.all()
    return render(request, 'shop/home.html', {'chocolates': chocolates})
