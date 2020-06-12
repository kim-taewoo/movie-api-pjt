from rest_framework import serializers
from .models import Movie, Country, Genre, Actor, Director, Review
from users.serializers import UserSerializer

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

class MiniMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'poster',
        )


class ReviewSerializer(serializer.ModelSerializer):
    creator = UserSerializer(read_only=True)
    movie = MiniMovieSerializer(read_only=True)
    is_liked = serializers.SerializerMethodField()
    is_unliked = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = (
            'id',
            'rating',
            'content',
            'creator',
            'movie',
            'formatted_time',
            'likes_count',
            'unlikes_count',
            'is_liked',
            'is_unliked',
        )

    def get_is_liked(self, obj):
        if 'request' in self.context:
            request = self.context['request']
            if obj in request.user.liked_reviews.all():
                return True;
        return False

    def get_is_unliked(self, obj):
        if 'request' in self.context:
            request = self.context['request']
            if obj in request.user.unliked_reviews.all():
                return True;
        return False
    
