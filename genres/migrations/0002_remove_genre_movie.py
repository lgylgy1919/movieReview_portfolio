# Generated by Django 3.1.6 on 2021-02-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='movie',
        ),
    ]
