from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Seller
from .forms import *

from shop.models import Shop
from product.models import Product
from order.models import Order


def sellerList(request):
    sellers = Seller.objects.all()

    context = {
        'sellers': sellers
    }
    return render(request, 'seller/seller_list.html', context)


def registerSeller(request):
    form = CreateSellerForm()

    if request.method == 'POST':
        form = CreateSellerForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name='seller')
            user.groups.add(group)

            Seller.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('seller_list')

    context = {
        'form': form
    }
    return render(request, 'seller/register_seller.html', context)


def updateSeller(request, pk=None):
    seller = Seller.objects.get(id=pk)
    form = SellerForm(instance=seller)

    if request.method == 'POST':
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_list')

    context = {
        'form': form
    }
    return render(request, 'seller/update_seller.html', context)


def deleteSeller(request, pk=None):
    seller = User.objects.get(id=pk)
    if request.method == "POST":
        seller.delete()
        return redirect('seller_list')

    context = {
        'seller': seller
    }
    return render(request, 'seller/delete_seller.html', context)
