from django.db import models
# import timedelta

class Artist(models.Model):
    name = models.CharField(max_length=500, null=True)
    biography = models.TextField(blank=True)
    img = models.URLField(max_length=200, blank=True)
    # songs = models.ManyToManyField('Song')
    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    songs = models.ManyToManyField('Song')

class Song(models.Model):
    name = models.CharField(max_length=500, null=True)
    duration = models.DurationField()
    # duration = models.DurationField(default="00:30:00", null=True)
    album = models.ForeignKey('Album', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.name
    
    
class Album(models.Model):
    name  = models.CharField(max_length=500, null=False, blank=False)
    publish_date = models.DateField(null=True)
    cover_art = models.URLField(max_length=200, null=True)
    album_genre = models.ManyToManyField('Genre')
    artist = models.ManyToManyField('Artist')
    # artist = models.ForeignKey('Artist', on_delete=models.PROTECT)
    def __str__(self):
        return self.artist

class Genre(models.Model):
    name = models.CharField(max_length=500, null=False)
    def __str__(self):
        return self.name


    
