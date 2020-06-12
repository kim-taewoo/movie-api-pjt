from rest_framework import serializers
from .models import Movie, Country, Genre, Actor, Director

class NationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', )


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name', )


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ('id', 'name', )


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    nations = NationSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'sub_title',
            'poster',
            'rating',
            'pub_date',
            'runtime',
            'overview',
            'audits',
            'audi_cnt',
            'genres',
            'actors',
            'directors',
            'nations',
        )