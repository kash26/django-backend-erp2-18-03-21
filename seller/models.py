from django.db import models
from django.contrib.auth.models import User

from shop.models import Shop


class Seller(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    shop = models.ForeignKey(Shop, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
