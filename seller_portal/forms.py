from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from order.models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['shop', 'seller', 'product', 'description']
        exclude = ['shop', 'seller']
