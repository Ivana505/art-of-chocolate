import json
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, View
#from django.views import generic
#import stripe
#from django.conf import settings
from django.views.generic import DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import *
from shop.forms import ChocolateForm
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY

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
    # 'stripe_public_key': 'pk_test_51LC4NEBJ4dJMxFfPk2Y6VvPLmEJxe7xhV7uiWu14rtiDetAkMgDpze0zDtvByNy6zYGKLk3VhyCkjL5dlRsg233H00ZkBo6tIK',
    # 'client_secret': 'test client secret'
    return render(request, 'shop/basket.html', context)


@login_required
def checkout(request):
    # stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # stripe_secret_key = settings.STRIPE_SECRET_KEY

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
            return redirect("shop")
        else:
            print(chocolate_form.errors)
    template = 'add_chocolate.html'
    context = {
            'chocolate_form': chocolate_form,
        }
    return render(request, template, context)




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


# class CreateCheckoutSessionVie(View):
#     def post(self, request, *args, **kwargs):
#         checkout_session = stripe.checkout.Session.create(
#            payment_method_types=['card'],
#            line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'eur',
#                         'name': 'Chocolates',


                
                    
#                 },
#             ],
#             'quantity': 1,
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success.html',
#             cancel_url=YOUR_DOMAIN + '/cancel.html',
#         )
#     except Exception as e:
#         return str(e)

#     return redirect(checkout_session.url, code=303)

# if __name__ == '__main__':
#     app.run(port=4242)


#@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)