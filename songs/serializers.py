from rest_framework import serializers
from .models import Artist,Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Artist
        fields = ['name']


class SongSerializer(serializers.ModelSerializer):
    artist =ArtistSerializer()
    class Meta:
        model = Song
        # fields = '__all__'
        fields = ['id','title','artist','listened_count']