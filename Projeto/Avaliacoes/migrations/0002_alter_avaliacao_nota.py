# Generated by Django 3.2.3 on 2021-05-13 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
