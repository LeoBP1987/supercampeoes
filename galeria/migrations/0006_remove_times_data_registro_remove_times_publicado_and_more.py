# Generated by Django 5.0.6 on 2024-06-09 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_times_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='times',
            name='data_registro',
        ),
        migrations.RemoveField(
            model_name='times',
            name='publicado',
        ),
        migrations.RemoveField(
            model_name='times',
            name='usuario',
        ),
    ]
