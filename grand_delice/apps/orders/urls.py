from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'form$', views.form, name='form'),
    url(r'add_order$', views.add_order, name='add_order'),
]
