# Generated by Django 3.2.3 on 2021-05-13 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Localizacoes', '0001_initial'),
        ('PontoTuristico', '0005_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Localizacoes.localizacao'),
            preserve_default=False,
        ),
    ]
