# Generated by Django 3.1.6 on 2021-02-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default='Add biography', max_length=100),
        ),
    ]
