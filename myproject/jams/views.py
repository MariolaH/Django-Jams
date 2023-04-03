from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Artist
from .models import Playlist
from .models import Song
from .serializer import ArtistSerializer, PlaylistSerializer, SongSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# Create your views here.
