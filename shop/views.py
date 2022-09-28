import json
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
#from django.views import generic
#import stripe
#from django.conf import settings
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import *
from shop.forms import ChocolateForm


class home(TemplateView):
    template_name = 'home.html'


def shop(request):
    # if request.user.is_authenticated:
        # buyer = get_object_or_404(User, username=request.user.username)
        # order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        # items = order.orderitem_set.all()
        # basketItems = order.get_basket_items
    # else:
        # items = []
        # order = {'get_basket_total': 0, 'get_basket_items': 0, 'shipping': False}
        # basketItems = order['get_basket_items']

    chocolates = Chocolate.objects.all()
    context = {'chocolates': chocolates}
    # context = {'chocolates': chocolates, 'basketItems': basketItems}
    return render(request, 'shop/shop.html', context)


@login_required
def basket(request):

    if request.user.is_authenticated:
        #buyer = request.user.buyer
        buyer, created = Buyer.objects.get_or_create(user=request.user)
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
        order = {'get_basket_total': 0, 'get_basket_items': 0, 'shipping':False}
        basketItems = order['get_basket_items']

        for i in basket:
            basketItems += basket[i]["quantity"]

            chocolate = Chocolate.objects.get(id=i)
            total = (chocolate.price * basket[i]["quantity"])

            order['get.basket_total'] += total
            order['get.basket_items'] += basket[i]["quantity"]        

    context = {'items': items, 'order': order, 'basketItems': basketItems}
    return render(request, 'shop/basket.html', context)


@login_required
def checkout(request):
    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete= False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items = []
        order = {'get_basket_total': 0, 'get_basket_items': 0, 'shipping': False}
        basketItems = order['get_basket_items']

    context = {'items': items, 'order': order, 'basketItems': basketItems}
    return render(request, 'shop/checkout.html', context)


@login_required
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
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_basket_total:
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
    chocolate = Chocolate.objects.filter(id=id).first()

    context = {
        'chocolate': chocolate,
    }

    return render(request, 'shop/chocolate_page.html', context)


# stripe.api_key = settings.STRIPE_SECRET_KEY

# class CreateCheckoutSessionView(generic.View):
#     def post(self, *args, **kwargs):
#         host = self.request.get_host()
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'eur',
#                         'unit_amount': 1000,
#                         'chocolate_data': {
#                             'name': 'codepiep-order',

#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url="http://{}{}".format(host, reverse('order:payment-success')),
#             cancel_url="http://{}{}".format(host, reverse('order:payment-cancel')),
#         )
#         return redirect(checkout_session.url, code=303)


# def paymentSuccess(request):
#     context = {
#         'payment_status': 'success'
#     }
#     return render(request, '/confirmation.html', context)


# def paymentCancel(request):
#     context = {
#         'payment_status': 'cancel'
#     }
#     return render(request, '/confirmation.html', context)


class DeleteProductView(DeleteView):
    model = Chocolate
    template_name = 'delete_chocolate.html'
    success_url = reverse_lazy('shop')


@login_required
def add_product(request):
    # add the request.FILES
    chocolate_form = ChocolateForm(request.POST, request.FILES)
    user = get_object_or_404(User, username=request.user.username)
    if request.method == "POST":
        if chocolate_form.is_valid():
            # save the form but do not commit
            form = chocolate_form.save(commit=False)
            # attach the arthur after
            form.author = request.user
            # save the form
            form.save()
            messages.success(request, "chocolate added")
            return redirect("home")
        else:
            print(chocolate_form.errors)
    template = 'add_chocolate.html'
    context = {
            'chocolate_form': chocolate_form,
        }
    return render(request, template, context)


# def edit_product(request, chocolate_id):
#     #chocolate = get_object_or_404(Chocolate, slug=slug)
#     chocolate = get_object_or_404(Chocolate, pk=chocolate_id)
#     if request.method == 'POST':
#         chocolate_form = ChocolateForm(request.POST, request.FILES, instance=chocolate)
#         if chocolate_form.is_valid():
#             form = chocolate_form.save(commit=False)
#             form.save()
#             messages.success(request, "chocolate edited")
#             return redirect(reverse('home', args=[chocolate.id]))
#     template = 'edit_chocolate.html'
#     context = {
#         'chocolate': chocolate,
#         'chocolate_form': chocolate_form,
#     }
#     return render(request, template, context)

# def edit_product(request, chocolate_id):
#     # add the request.FILES
#     chocolate_form = ChocolateForm(request.POST, request.FILES)
#     user = get_object_or_404(User, username=request.user.username)
#     if request.method == "POST":
#         if chocolate_form.is_valid():
#             # save the form but do not commit
#             form = chocolate_form.save(commit=True)
#             # attach the arthur after
#             form.author = request.user
#             # save the form
#             form.save()
#             messages.success(request, "edited")
#             return redirect("home")
#         else:
#             print(chocolate_form.errors)
#     template = 'edit_chocolate.html'
#     context = {
#             'chocolate_form': chocolate_form,
#         }
#     return render(request, template, context)


@login_required
def edit_product(request, pk):
    # add the request.FILES
    chocolate = get_object_or_404(Chocolate, id=pk)
    chocolate_form = ChocolateForm(request.POST, request.FILES)
    user = get_object_or_404(User, username=request.user.username)
    if request.method == "POST":
        if chocolate_form.is_valid():
            # save the form but do not commit
            form = ChocolateForm(request.POST, request.FILES, instance=chocolate)
            # attach the arthur after
            if form.is_valid():
                form.save()
                messages.success(request, "edited")
                return redirect(reverse('chocolate_page', args=[chocolate.id]))
    else:
        form = ChocolateForm(instance=chocolate)
        messages.error(request, f'youre updating {chocolate.name}')

    template = 'edit_chocolate.html'
    context = {
            'form': form,
            'chocolate': chocolate,
        }
    return render(request, template, context)
