from django.forms import ModelForm
from django import forms

from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
