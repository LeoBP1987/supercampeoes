# Generated by Django 5.0.6 on 2024-06-09 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonatos', '0004_alter_campeonato_principal'),
        ('galeria', '0014_remove_times_titulos'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeclararCampeao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonatos.campeonato')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.times')),
            ],
        ),
    ]