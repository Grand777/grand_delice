# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from grand_delice.apps.products.models import *
from django.core.validators import RegexValidator
from django.db.models.signals import post_save


# Create your models here.


class IndividualComposition(models.Model):
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    customer_phone_number = models.CharField(verbose_name='Номер телефона', validators=[customer_phone_regex], blank=True, max_length=15, default=None)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    box_size = models.CharField(max_length=64, blank=True, null=True, default=None)
    box_color = models.CharField(max_length=64, blank=True, null=True, default=None)
    composition_color = models.CharField(max_length=64, blank=True, null=True, default=None)
    flower_preference = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return 'Индивидуальная композиция %s' % self.id

    class Meta:
        verbose_name = 'Индивидуальная композиция'
        verbose_name_plural = 'Индивидуальные композиции'




