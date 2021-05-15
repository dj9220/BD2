# Generated by Django 3.0.8 on 2021-05-12 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0049_auto_20210511_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]