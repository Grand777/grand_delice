from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'online_boutique$', views.online_boutique, name='online_boutique'),
]