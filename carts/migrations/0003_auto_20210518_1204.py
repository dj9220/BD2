# Generated by Django 3.0.8 on 2021-05-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0055_auto_20210516_1631'),
        ('carts', '0002_remove_cart_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='shop.Product'),
        ),
    ]