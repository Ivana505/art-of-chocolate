from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=40, null=True)
    email_address = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.name
