# Generated by Django 3.1.6 on 2021-02-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210223_0928'),
        ('genres', '0003_genre_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='test',
            field=models.ManyToManyField(related_name='test', to='movies.Movie'),
        ),
    ]
