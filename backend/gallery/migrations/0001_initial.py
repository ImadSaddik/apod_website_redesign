# Generated by Django 4.2.4 on 2023-08-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('explanation', models.TextField()),
                ('image_url', models.CharField(max_length=150)),
                ('keywords', models.ManyToManyField(to='gallery.keyword')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
