# Generated by Django 3.2.3 on 2021-05-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atracoes', '0001_initial'),
        ('PontoTuristico', '0002_alter_pontoturistico_aprovado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='Atracoes.Atracao'),
        ),
    ]
