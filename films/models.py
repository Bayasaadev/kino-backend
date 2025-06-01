from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=60, unique=True)
    code = models.CharField(max_length=4, unique=True)
    flag = models.ImageField(upload_to='flags/', blank=True, null=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    founded_year = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Film(models.Model):
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200, blank=True)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(blank=True, null=True)  # in minutes
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    background = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    trailer_url = models.URLField(blank=True)
    release_date = models.DateField(blank=True, null=True)

    genres = models.ManyToManyField(Genre, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)
    studios = models.ManyToManyField(Studio, blank=True)
    countries = models.ManyToManyField(Country, blank=True)
    languages = models.ManyToManyField(Language, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})"