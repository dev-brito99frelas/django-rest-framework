# Generated by Django 3.2.3 on 2021-05-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=2)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
