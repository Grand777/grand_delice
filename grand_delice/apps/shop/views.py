from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from grand_delice.apps.products.models import *
from grand_delice.apps.cart.forms import CartAddProductForm


def index(request):


    data_name = Product

    context = {
        'data_nam': data_name
    }

    return render(request, 'shop/html/index.html', locals())


def online_boutique(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)



    return render(request, 'products/html/products.html', locals())

def ProductDetail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()
    return render_to_response('shop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})
