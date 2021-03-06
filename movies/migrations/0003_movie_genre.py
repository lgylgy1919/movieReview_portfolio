# Generated by Django 3.1.6 on 2021-02-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0005_auto_20210223_1434'),
        ('movies', '0002_auto_20210223_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='genres.Genre'),
        ),
    ]
