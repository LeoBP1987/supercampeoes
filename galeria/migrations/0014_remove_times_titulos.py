# Generated by Django 5.0.6 on 2024-06-09 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0013_remove_times_titulos_times_titulos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='times',
            name='titulos',
        ),
    ]