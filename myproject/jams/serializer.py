from rest_framework import serializers
from .models import Artist
from .models import Playlist
from .models import Song
from .models import Album
from .models import Genre
from django.contrib.auth.models import User, Group

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'publish_date', 'cover_art', 'album_genre']

class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(many=True, required=False)
    class Meta:
        model = Song
        fields = ['id','name', 'duration', 'album']

class ArtistSerializer(serializers.ModelSerializer):
    # songs = SongSerializer(many=True, required=False)
    class Meta:
        model = Artist
        fields = ['id','name', 'biography', 'img', 'songs']

class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, required=False)
    class Meta:
        model = Playlist
        fields = ['id','name', 'songs']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']