# Generated by Django 4.1 on 2022-09-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_rename_movie_rating_mywatchlistitem_movie_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlistitem',
            name='watched_movie',
            field=models.CharField(max_length=255),
        ),
    ]
