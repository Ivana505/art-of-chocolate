from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

def shop(request):

    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_item':0, 'shipping':False}
        basketItems = order['get_basket_items']

    chocolates = Chocolate.objects.all()
    context = {'chocolates' :chocolates, 'basketItems' :basketItems}
    return render(request, 'shop/shop.html', context)

def basket(request):

    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_item':0, 'shipping':False}
        basketItems = order['get_basket_items']

    context = {'items': items, 'order':order, 'basketItems' :basketItems}
    return render(request, 'shop/basket.html', context)


def checkout(request):
    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_item':0, 'shipping':False}
        basketItems = order['get_basket_items']

    context = {'items': items, 'order':order, 'basketItems' :basketItems}
    return render(request, 'shop/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    chocolateId = data['chocolateId']
    action = data['action']

    print('Action', action)
    print('chocolateId', chocolateId)

    buyer = request.user.buyer
    chocolate = Chocolate.objects.get(id=chocolateId)
    order, created = Order.objects.get_or_create(buyer=buyer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, chocolate=chocolate)


    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added', safe=False)
