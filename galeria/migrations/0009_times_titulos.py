# Generated by Django 5.0.6 on 2024-06-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonatos', '0004_alter_campeonato_principal'),
        ('galeria', '0008_times_data_registro_times_publicado_times_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='times',
            name='titulos',
            field=models.ManyToManyField(related_name='titulos', to='campeonatos.campeonato'),
        ),
    ]