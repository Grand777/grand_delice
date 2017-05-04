from django.shortcuts import render
from .models import *


# Create your views here.


def AddOrder(request):
    data = request.POST
    print(data)
    return render(request, 'form.html')


def form(request):
    return render(request, 'form.html')
