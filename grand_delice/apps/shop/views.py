from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from grand_delice.apps.products.models import *


def home(request):

    return render(request, 'shop/html/home.html', locals())


def online_boutique(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'shop/html/online_boutique.html', locals())


def cart(request):
    return render(request, 'shop/html/cart.html', locals())


def composition(request):

    return render(request, 'shop/html/composition.html', locals())


def discount(request):

    return render(request, 'shop/html/discount.html', locals())


def delivery(request):

    return render(request, 'shop/html/delivery.html', locals())
