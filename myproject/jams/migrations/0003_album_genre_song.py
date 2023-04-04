# Generated by Django 4.2 on 2023-04-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0002_playlist_alter_artist_biography_alter_artist_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('publish_date', models.DateField()),
                ('cover_art', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('duration', models.DurationField()),
            ],
        ),
    ]