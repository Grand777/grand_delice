from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'form$', views.form, name='form'),
    url(r'addorder$', views.AddOrder, name='AddOrder'),
]
