from django.contrib import admin
from .models import Category, Chocolate

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Chocolate)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock']
    list_editavel = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}
