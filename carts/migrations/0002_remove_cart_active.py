# Generated by Django 3.0.8 on 2021-05-18 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='active',
        ),
    ]