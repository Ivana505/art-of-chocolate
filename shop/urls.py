from django.urls import path
from . import views
from contact.views import contact


urlpatterns = [
    path('', views.shop, name="shop"),
    path('basket/', views.basket, name="basket"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path(
        'chocolate_page/<str:id>',
        views.chocolate_page, name="chocolate_page"),
    path(
        'delete_chocolate/<pk>',
        views.DeleteProductView.as_view(), name="delete_chocolate"),
    path('add_chocolate/', views.add_product, name="add_chocolate"),
    path('edit_chocolate/<pk>', views.edit_product, name="edit_chocolate"),
    path(
        'create-checkout-session',
        views.CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'),
    path('payment-success/', views.paymentSuccess, name='payment-success'),
    path('payment-cancel/', views.paymentCancel, name='payment-cancel'),
    path('webhook/stripe', views.my_webhook_view, name='webhook-stripe'),
    path('category/<int:category>', views.shop, name='category'),
]
