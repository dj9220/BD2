# Generated by Django 3.1.7 on 2021-03-17 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.subcategories'),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]
