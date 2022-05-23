from django.shortcuts import render
from .models import *
# Create your views here.


def cart(requests):
    ctx = {}
    return render(requests, 'cart.html', ctx)


def catalog(requests):
    product = Product.objects.all()
    ctg = Category.objects.all()
    ctx = {
        'product': product,
        'ctg': ctg
    }
    return render(requests, 'catalog.html', ctx)


def compare(requests):
    ctx = {}
    return render(requests, 'compare.html', ctx)


def contacts(requests):
    ctx = {}
    return render(requests, 'contacts.html', ctx)


def index(requests):
    ctx = {}
    return render(requests, 'index.html', ctx)


def product(requests, pk):
    product = Product.objects.get(pk=pk)
    ctx = {'product': product}
    return render(requests, 'product.html', ctx)

