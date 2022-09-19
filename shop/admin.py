from django.contrib import admin
from .models import *

admin.site.register(Buyer)
admin.site.register(Chocolate)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(SendingAddress)
