from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Shop
from .forms import *

from order.models import Order
from product.models import Product
from seller.models import Seller


def home(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    sellers = Seller.objects.all()
    shops = Shop.objects.all()

    context = {
        'orders': orders,
        'products': products,
        'sellers': sellers,
        'shops': shops
    }
    return render(request, "shop/dashboard.html", context)


def shopList(request):
    shops = Shop.objects.all()

    context = {
        'shops': shops
    }
    return render(request, "shop/shops_list.html", context)


def registerShop(request):
    form = CreateShopForm()

    if request.method == 'POST':
        form = CreateShopForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name='admin')
            user.groups.add(group)

            Shop.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'shop/register_shop.html', context)


def updateShop(request, pk=None):
    shop = Shop.objects.get(id=pk)
    form = ShopForm(instance=shop)

    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_list')

    context = {
        'form': form
    }
    return render(request, 'shop/update_shop.html', context)
