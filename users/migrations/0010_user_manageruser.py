# Generated by Django 3.1.6 on 2021-02-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='manageruser',
            field=models.BooleanField(default=False),
        ),
    ]
