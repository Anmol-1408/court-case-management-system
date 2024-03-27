# Generated by Django 4.2.11 on 2024-03-27 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mydashboard', '0002_remove_clientrecord_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
