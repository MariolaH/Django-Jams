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

class ArtistNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name']

class AlbumReadSerializer(serializers.ModelSerializer):
    artist = ArtistNameSerializer(many=True)
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

class SongNameSerializer(serializers.ModelSerializer):
    artists = serializers.SerializerMethodField()
        # SerialzerMethodField = gets its value by calling a method on the serializer class it is attached to
        # artists is what is storing the id and name of the artist

    class Meta:
        model = Song
        fields = ['id', 'name', 'artists']

    # https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    def get_artists(self, obj):

        album = Album.objects.get(pk=obj.album_id)
            # Retrieving a single object with get() - getting album primary key
        artists = album.artist.all()
            # through the album PK getting all the artist fields
            # artists is = going through the albums model (which has a m2m relationship with artist)to 
            # artist(gets all the fields)
 
        # shorthand to create a list with a loop inside of it
        # https://stackoverflow.com/a/67384477
        return [{ "id": a.id, "name": a.name } for a in artists]
            # returning only the id and name of the artist


class PlaylistReadSerializer(serializers.ModelSerializer):
    songs = SongNameSerializer(many=True, required=False)
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