# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_productinorder_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='customer_phone_number',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='delivery_time',
        ),
    ]
