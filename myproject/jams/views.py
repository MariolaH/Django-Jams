from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Artist
from .models import Playlist
from .models import Song
from .models import Album
from .models import Genre
from .serializer import ArtistSerializer, PlaylistSerializer, SongSerializer,AlbumSerializer, GenreSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
# Create your views here.
