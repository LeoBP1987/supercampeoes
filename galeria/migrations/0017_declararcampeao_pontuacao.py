# Generated by Django 5.0.6 on 2024-06-09 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0016_times_titulos'),
    ]

    operations = [
        migrations.AddField(
            model_name='declararcampeao',
            name='pontuacao',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
