from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Chocolate(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)



    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=150, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_basket_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_basket_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    


class OrderItem(models.Model):
    chocolate = models.ForeignKey(Chocolate, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.chocolate.price * self.quantity
        return total


class SendingAddress(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    zipcode = models.CharField(max_length=255, null=False)
    date_added = models.CharField(max_length=255, null=False)


    def __str__(self):
        return self.address

#     author = models.CharField(max_length=255, default='admin')
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/')
#     slug = models.SlugField(max_length=255)
#     in_stock = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = 'Chocolates'
#         ordering = ('-created',)

#     def get_absolute_url(self):
#         return reverse('shop:chocolate_detail', args=[self.slug])

#     def __str__(self):
#         return self.name


# class Category(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True)

#     class Meta:
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name

# class Chocolate(models.Model):
#     category = models.ForeignKey(Category, related_name='chocolate', on_delete=models.CASCADE)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
#     name = models.CharField(max_length=255)
#     author = models.CharField(max_length=255, default='admin')
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/')
#     slug = models.SlugField(max_length=255)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#     in_stock = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


#     class Meta:
#         verbose_name_plural = 'Chocolates'
#         ordering = ('-created',)

#     def get_absolute_url(self):
#         return reverse('shop:chocolate_detail', args=[self.slug])

#     def __str__(self):
#         return self.name
