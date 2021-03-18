from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from seller.models import Seller
from .forms import *

from shop.models import Shop
from product.models import Product
from order.models import Order


def sellerLoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('seller_portal_list')
        else:
            # messages.info(request, 'username OR Password is incorrect')
            return HttpResponse("You cannot access the seller page!")

    context = {}
    return render(request, 'seller_portal/login.html', context)


def orderList(request):
    orders = request.user.seller.order_set.all()
    seller = request.user.seller
    seller_id = Seller.objects.get(name=seller)

    context = {
        'orders': orders,
        'seller_id': seller_id
    }
    return render(request, 'seller_portal/order_list.html', context)


def createOrder(request, pk=None):
    user_seller = request.user.seller
    seller = Seller.objects.get(id=pk)
    shop = seller.shop
    form = OrderForm(initial={'shop': shop, 'seller': user_seller})

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=True)
            instance.seller = user_seller
            instance.shop = shop
            form.save()
            return redirect('seller_portal_list')

    context = {
        'form': form
    }
    return render(request, 'seller_portal/order_form.html', context)


def updateOrder(request, pk=None):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')

    context = {
        'form': form
    }
    return render(request, 'order/order_form.html', context)


def deleteOrder(request, pk=None):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('order_list')

    context = {
        'item': order
    }
    return render(request, 'order/delete_order.html', context)