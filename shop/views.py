from django.shortcuts import get_object_or_404, render

from .models import Category, Chocolate

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_chocolates(request):
    chocolates = Chocolate.objects.all()
    return render(request, 'shop/home.html', {'chocolates': chocolates})

def chocolate_detail(request, slug):
    chocolate = get_object_or_404(Chocolate, slug=slug, in_stock=True)
    return render(request, 'shop/chocolates/detail.html', {'chocolate': chocolate})