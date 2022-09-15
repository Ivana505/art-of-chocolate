from django.contrib import admin
from .models import Chocolates, Category

class ChocolatesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image'
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Chocolates, ChocolatesAdmin)
admin.site.register(Category, CategoryAdmin)
