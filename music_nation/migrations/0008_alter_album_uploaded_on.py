# Generated by Django 4.1 on 2022-08-29 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0007_remove_song_artist_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2022, 8, 29, 19, 27, 20, 43210, tzinfo=datetime.timezone.utc)),
        ),
    ]
