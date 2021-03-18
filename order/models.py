from django.db import models

from product.models import Product
from seller.models import Seller
from shop.models import Shop


class Order(models.Model):
    shop = models.ForeignKey(Shop, null=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name
