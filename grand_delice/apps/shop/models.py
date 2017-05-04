# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(verbose_name='Номер телефона', validators=[phone_regex], blank=True, max_length=15)

    def __str__(self):
        return 'Клиент %s %s %s' % (self.id, self.name, self.phone_number)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
