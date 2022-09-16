from django.shortcuts import render
from .models import Chocolates


def all_chocolates(request):
    """ return to the index page """
   # chocolates = Chocolate.objects.all()
   # return render(request, 'home/index.html', {'chocolates': chocolates})

    chocolates = Chocolates.objects.all()

    context = {
        'chocolates' : chocolates,
    }


    return render(request, 'chocolates/chocolates.html', context)
