from rest_framework import serializers
from .models import Genre, Theme, Country, Language, Studio, Film

# 1. Genre serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']

# 2. Theme serializer
class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'name', 'description']

# 3. Country serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code', 'flag']

# 4. Language serializer
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'code']

# 5. Studio serializer
class StudioSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), source='country', write_only=True, required=False
    )
    class Meta:
        model = Studio
        fields = ['id', 'name', 'description', 'founded_year', 'country', 'country_id']

# 6. Film serializers
class FilmListSerializer(serializers.ModelSerializer):
    poster = serializers.ImageField(read_only=True)

    class Meta:
        model = Film
        fields = [
            'id', 'title', 'year', 'poster'
        ]

class FilmDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    themes = ThemeSerializer(many=True, read_only=True)
    studios = StudioSerializer(many=True, read_only=True)
    countries = CountrySerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    poster = serializers.ImageField(read_only=True)
    background = serializers.ImageField(read_only=True)

    class Meta:
        model = Film
        fields = [
            'id', 'title', 'original_title', 'tagline', 'year', 
            'description', 'duration', 'poster', 'background', 
            'trailer_url', 'release_date', 'genres', 'themes', 'studios',
            'countries', 'languages', 'created_at', 'updated_at'
        ]

class FilmCreateUpdateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, required=False)
    themes = serializers.PrimaryKeyRelatedField(queryset=Theme.objects.all(), many=True, required=False)
    studios = serializers.PrimaryKeyRelatedField(queryset=Studio.objects.all(), many=True, required=False)
    countries = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), many=True, required=False)
    languages = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True, required=False)
    poster = serializers.ImageField(required=False)
    background = serializers.ImageField(required=False)

    class Meta:
        model = Film
        fields = [
            'id', 'title', 'original_title', 'tagline', 'year', 
            'description', 'duration', 'poster', 'background', 
            'trailer_url', 'release_date', 'genres', 'themes', 
            'studios', 'countries', 'languages'
        ]
