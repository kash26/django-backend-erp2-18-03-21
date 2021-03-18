from django.db import models

from shop.models import Shop


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    shop = models.ForeignKey(Shop, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
