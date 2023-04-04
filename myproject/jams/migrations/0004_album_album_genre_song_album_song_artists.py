# Generated by Django 4.2 on 2023-04-04 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0003_album_genre_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_genre',
            field=models.ManyToManyField(to='jams.genre'),
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='jams.album'),
        ),
        migrations.AddField(
            model_name='song',
            name='artists',
            field=models.ManyToManyField(to='jams.artist'),
        ),
    ]
