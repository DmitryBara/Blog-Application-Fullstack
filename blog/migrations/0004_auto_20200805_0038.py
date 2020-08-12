# Generated by Django 3.0.8 on 2020-08-04 21:38

import blog.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20200804_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='rating',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='art_to_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]