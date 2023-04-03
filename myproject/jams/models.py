from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=500)
    biography = models.TextField()
    img = models.URLField(max_length=200)


