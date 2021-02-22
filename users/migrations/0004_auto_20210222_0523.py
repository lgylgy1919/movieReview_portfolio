# Generated by Django 3.1.6 on 2021-02-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210221_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='reviews',
            field=models.CharField(default='Reviews what you wrote', max_length=100),
        ),
    ]
