# Generated by Django 3.0.8 on 2021-04-25 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0017_auto_20210425_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
