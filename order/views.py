from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Order
from .forms import OrderForm

from shop.models import Shop
from product.models import Product
from seller.models import Seller


def orderList(request):
    orders = Order.objects.all()

    context = {
        'orders': orders
    }
    return render(request, 'order/order_list.html', context)


def createOrder(request, pk=None):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')

    context = {
        'form': form
    }
    return render(request, 'order/order_form.html', context)


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