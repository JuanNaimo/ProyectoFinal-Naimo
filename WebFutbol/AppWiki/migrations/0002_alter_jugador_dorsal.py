# Generated by Django 4.0.4 on 2022-07-23 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='dorsal',
            field=models.IntegerField(),
        ),
    ]
