# Generated by Django 2.0.6 on 2018-12-09 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='mid',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]