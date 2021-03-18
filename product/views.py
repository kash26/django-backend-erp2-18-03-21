from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm

from shop.models import Shop
from order.models import Order
from seller.models import Seller


def productList(request):
    products = Product.objects.all()
    print(products)

    context = {
        'products': products
    }
    return render(request, 'product/product_list.html', context)


def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    context = {
        'form': form
    }
    return render(request, 'product/product_form.html', context)


def updateProduct(request, pk=None):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    context = {
        'form': form
    }
    return render(request, 'product/product_form.html', context)


def deleteProduct(request, pk=None):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    context = {
        'item': product
    }
    return render(request, 'product/delete_product.html', context)