# Generated by Django 3.0.8 on 2021-05-16 13:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0052_auto_20210516_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='price_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
