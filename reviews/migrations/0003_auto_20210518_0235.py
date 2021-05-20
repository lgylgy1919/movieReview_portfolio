# Generated by Django 3.1.6 on 2021-05-18 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_movie_reviews'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_auto_20210506_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]