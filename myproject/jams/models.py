from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    biography = models.TextField(blank=True)
    img = models.URLField(max_length=200, blank=True)

class Playlist(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)

class Song(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    duration = models.DurationField(null=False, blank=False)
    


    
