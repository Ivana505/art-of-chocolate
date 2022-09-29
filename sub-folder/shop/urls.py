from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_chocolates, name='all_chocolates'),
    path('chocolate/<slug:slug>/', views.chocolate_detail, name='chocolate_detail'),
]