# Generated by Django 4.1 on 2022-09-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched_movie', models.BooleanField()),
                ('movie_name', models.CharField(max_length=255)),
                ('movie_rating', models.IntegerField()),
                ('release_date', models.DateField()),
                ('movie_review', models.CharField(max_length=255)),
            ],
        ),
    ]
