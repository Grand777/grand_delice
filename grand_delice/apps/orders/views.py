from itertools import product

from django.core import serializers
from django.shortcuts import render
from .models import *
from django.forms import ModelForm


# Create your views here.


def add_order(request):
    data = request.POST
    data.dict()
    print (data)
    if data:
        # IndividualComposition.objects.create(data.get('customer_name', 'customer_phone_number', 'customer_email'))
        model = IndividualComposition()
        model.customer_name = data.get('customer_name')
        model.customer_phone_number = data.get('customer_phone_number')
        model.customer_email = data.get('customer_email')
        model.box_size = BoxSize.objects.create(size=data.get('box_size'))
        model.box_color = BoxColor.objects.create(color=data.get('box_color'))
        model.save()

    print(data)

    return render(request, 'form.html')


def form(request):
    return render(request, 'form.html', locals())
