# Generated by Django 3.0.8 on 2021-04-20 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_check_supplier'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Matts',
        ),
        migrations.RemoveField(
            model_name='product',
            name='matt',
        ),
    ]
