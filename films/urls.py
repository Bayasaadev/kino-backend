from django.urls import path
from .views import (
    GenreListCreateView, 
    GenreRetrieveUpdateDestroyView,
    ThemeListCreateView,
    ThemeRetrieveUpdateDestroyView,
    CountryListCreateView,
    CountryRetrieveUpdateDestroyView,
    LanguageListCreateView,
    LanguageRetrieveUpdateDestroyView,
    StudioListCreateView,
    StudioRetrieveUpdateDestroyView,
    FilmListCreateView,
    FilmRetrieveUpdateDestroyView
)

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
    path('themes/', ThemeListCreateView.as_view(), name='theme-list-create'),
    path('themes/<int:pk>/', ThemeRetrieveUpdateDestroyView.as_view(), name='theme-detail'),
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),
    path('languages/', LanguageListCreateView.as_view(), name='language-list-create'),
    path('languages/<int:pk>/', LanguageRetrieveUpdateDestroyView.as_view(), name='language-detail'),
    path('studios/', StudioListCreateView.as_view(), name='studio-list-create'),
    path('studios/<int:pk>/', StudioRetrieveUpdateDestroyView.as_view(), name='studio-detail'),
    path('films/', FilmListCreateView.as_view(), name='film-list-create'),
    path('films/<int:pk>/', FilmRetrieveUpdateDestroyView.as_view(), name='film-detail'),
]
