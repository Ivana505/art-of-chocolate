from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
import json
from .models import *
import datetime

class home(TemplateView):
    template_name = 'home.html'

def shop(request):

    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_items':0, 'shipping':False}
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
        try:
            basket = json.loads(request.COOKIES['basket'])
        except:
           basket = {}
           print('Basket:', basket)
        items = []
        order = {'get_basket_total':0, 'get_basket_items':0, 'shipping':False}
        basketItems = order['get_basket_items']

        for i in basket:
            basketItems += basket[i]["quantity"]

            chocolate = Chocolate.objects.get(id=i)
            total = (chocolate.price * basket[i]["quantity"])

            order['get.basket_total'] += total
            order['get.basket_items'] += basket[i]["quantity"]
            

    context = {'items' :items, 'order' :order, 'basketItems':basketItems}
    return render(request, 'shop/basket.html', context)


def checkout(request):
    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_items':0, 'shipping':False}
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


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_basket_total :
            order.complete = True
        order.save()

        if order.shipping == True:
            SendingAddress.objects.create(
                buyer=buyer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],

            )

    else:
        print('You are not logged in.')
    return JsonResponse('You paid !', safe=False)


def chocolate_page(request, id):
    chocolate = Chocolate.objects.filter(id = id).first()

    context = {
        'chocolate':chocolate,
    }

    return render(request, 'shop/chocolate_page.html',context)