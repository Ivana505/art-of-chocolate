from django.shortcuts import render
#from shop.models import Chocolate



# Create your views here.
def index(request):
    """ return to the index page """
    chocolates = Chocolate.objects.all() 
    return render(request, 'home/index.html', {'chocolates': chocolates})