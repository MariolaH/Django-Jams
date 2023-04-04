from django.db import models
import timedelta

class Artist(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    biography = models.TextField(blank=True)
    img = models.URLField(max_length=200, blank=True)

class Playlist(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)

class Song(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    duration = models.DurationField()
    # duration = models.DurationField(default="00:30:00", null=True)
    
class Album(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    publish_date = models.DateField(null=False, blank=False)
    cover_art = models.URLField(max_length=200, blank=True)

class Genre(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)


    
