# Generated by Django 3.1.7 on 2021-03-17 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_subcategories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='subCategory',
        ),
    ]