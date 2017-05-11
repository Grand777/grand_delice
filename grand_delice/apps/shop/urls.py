from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'online_boutique$', views.online_boutique, name='online_boutique'),
    url(r'cart$', views.cart, name='cart'),
    url(r'composition$', views.composition, name='composition'),
    url(r'discount$', views.discount, name='composition'),

]
