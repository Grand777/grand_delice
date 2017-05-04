from django.shortcuts import render, get_object_or_404

from grand_delice.apps.cart.forms import CartAddProductForm
from .models import *


def product_item(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/html/product_item.html', {'product': product})

