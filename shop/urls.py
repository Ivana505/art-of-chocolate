from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('basket/', views.basket, name="basket"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('', views.home, name="home"),
    path('chocolate_page/<str:id>', views.chocolate_page, name="chocolate_page"),
    path('delete_chocolate/<pk>', views.DeleteProductView.as_view(), name="delete_chocolate"),
    #path('create-checkout-session', views.CreateCheckoutSessionView, name='create-checkout-session')
]
