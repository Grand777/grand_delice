# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from grand_delice.apps.products.models import *
from django.core.validators import RegexValidator
from django.db.models.signals import post_save


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Статус %s' % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class IndividualOrder(models.Model):
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    customer_phone_number = models.CharField(verbose_name='Номер телефона', validators=[customer_phone_regex], blank=True, max_length=15, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    customer_address = models.CharField(verbose_name='Адрес доставки', max_length=250, blank=True, null=True, default=None)
    delivery_time = models.DateTimeField(verbose_name='Время и дата доставки', auto_now_add=False,blank=True, null=True, default=None)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)
    status = models.ForeignKey(Status)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order

    def __str__(self):
        return 'Заказ %s %s %s %s' % (self.id, self.customer_name, self.customer_phone_number, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



class Order(models.Model):
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    customer_phone_number = models.CharField(verbose_name='Номер телефона', validators=[customer_phone_regex], blank=True, max_length=15, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    customer_address = models.CharField(verbose_name='Адрес доставки', max_length=250, blank=True, null=True, default=None)
    delivery_time = models.DateTimeField(verbose_name='Время и дата доставки', auto_now_add=False,blank=True, null=True, default=None)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)
    status = models.ForeignKey(Status)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order

    def __str__(self):
        return 'Заказ %s %s %s %s' % (self.id, self.customer_name, self.customer_phone_number, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    # customer_email = models.EmailField(blank=True, null=True, default=None)
    # customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    # customer_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    # customer_phone_number = models.CharField(verbose_name='Номер телефона', validators=[customer_phone_regex], blank=True, max_length=15, default=None)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    is_active = models.BooleanField(default=True)
    # address = models.CharField(verbose_name='Адрес доставки', max_length=250)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    # delivery_time = models.DateTimeField(verbose_name='Время и дата доставки', auto_now_add=False)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)

    def __str__(self):
        return '%s' % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance,created,**kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)


