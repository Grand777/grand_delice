from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^online_boutique/$', views.product_item, name='product_item'),
]
