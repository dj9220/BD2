# Generated by Django 3.0.8 on 2021-05-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_auto_20210509_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
