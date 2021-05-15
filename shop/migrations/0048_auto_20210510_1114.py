# Generated by Django 3.0.8 on 2021-05-10 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0047_auto_20210510_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(200.0), django.core.validators.MinValueValidator(0.01)]),
        ),
    ]