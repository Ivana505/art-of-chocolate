from django.shortcuts import render
# from django.http import JsonResponse
# import json
from .models import *

def shop(request):
    chocolates = Chocolate.objects.all()
    context = {'chocolates' :chocolates}
    return render(request, 'shop/shop.html', context)

def basket(request):

    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_item':0}

    context = {'items': items, 'order':order}
    return render(request, 'shop/basket.html', context)


def checkout(request):
    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_item':0}

    context = {'items': items, 'order':order}
    return render(request, 'shop/checkout.html', context)


# def updateItem(request):
#     return JsonResponse('Item was added', sale=False)

# def updateChocolate(request):
#     data = json.loads(request.data)
#     chocolateId = data['chocolateId']
#     action = data['action']

#     print('Action:', action)
#     print('chocolateId:', chocolateId)
#     return JsonResponse('Chocolate was added', safe=False)
