# Generated by Django 3.1.6 on 2021-05-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210518_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='Unknown', max_length=30, unique=True),
        ),
    ]
