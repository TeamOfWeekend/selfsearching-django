# Generated by Django 2.0.6 on 2018-12-12 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_film_mid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='mid',
        ),
    ]
