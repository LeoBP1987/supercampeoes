# Generated by Django 5.0.6 on 2024-06-09 14:53

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_times_simbolo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='times',
            name='data_registro',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='times',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='times',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usu', to=settings.AUTH_USER_MODEL),
        ),
    ]