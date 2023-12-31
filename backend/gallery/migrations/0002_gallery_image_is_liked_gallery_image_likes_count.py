# Generated by Django 4.2.4 on 2023-08-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image_is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image_likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
