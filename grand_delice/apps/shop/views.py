from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from grand_delice.apps.products.models import *


def home(request):
    return render(request, 'home.html', locals())


def online_boutique(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'products/html/online_boutique.html', locals())


def cart(request):
    return render(request, 'shop/html/cart.html', locals())
