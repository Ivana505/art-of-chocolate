from django.urls import path
from . import views

# app_name = 'shop'

# urlpatterns = [
#     path('', views.all_chocolates, name='all_chocolates'),
#     path('chocolate/<slug:slug>/', views.chocolate_detail, name='chocolate_detail'),
#]

urlpatterns = [
    path('', views.shop, name="shop"),
    path('basket/', views.basket, name="basket"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]
