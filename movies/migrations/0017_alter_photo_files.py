# Generated by Django 3.2.3 on 2021-06-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_alter_photo_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='files',
            field=models.ImageField(upload_to='poster'),
        ),
    ]
