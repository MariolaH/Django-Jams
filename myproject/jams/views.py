from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Artist
from .models import Playlist
from .models import Song
from .models import Album
from .models import Genre
from .serializer import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ArtistWriteSerializer
        return ArtistReadSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return PlaylistWriteSerializer
        return PlaylistReadSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return SongWriteSerializer
        return SongReadSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return AlbumWriteSerializer
        return AlbumReadSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
# Create your views here.
