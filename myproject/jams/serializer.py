from rest_framework import serializers
from .models import Artist
from .models import Playlist
from .models import Song
from .models import Album
from .models import Genre
from django.contrib.auth.models import User, Group

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']

class ArtistReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name', 'biography', 'img']

class ArtistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name', 'biography', 'img']

class AlbumReadSerializer(serializers.ModelSerializer):
    artist = ArtistReadSerializer(many=True)
    album_genre = GenreSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'artist', 'publish_date', 'cover_art', 'album_genre']


class AlbumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'publish_date', 'cover_art', 'album_genre']

class SongReadSerializer(serializers.ModelSerializer):
    album = AlbumReadSerializer()
    class Meta:
        model = Song
        fields = ['id','name', 'duration', 'album']

class SongWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','name', 'duration', 'album']


class PlaylistReadSerializer(serializers.ModelSerializer):
    songs = SongReadSerializer(many=True, required=False)
    class Meta:
        model = Playlist
        fields = ['id','name', 'songs']

class PlaylistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id','name', 'songs']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']