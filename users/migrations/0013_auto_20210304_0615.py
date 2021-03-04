# Generated by Django 3.1.6 on 2021-03-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('users', '0012_auto_20210222_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='reviews',
        ),
        migrations.AddField(
            model_name='user',
            name='reviews',
            field=models.ManyToManyField(blank=True, related_name='user', to='reviews.Review'),
        ),
    ]
