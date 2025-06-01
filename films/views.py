from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from users.permissions import IsRoleAdminOrStaff
from .models import Genre, Theme, Country, Language, Studio, Film
from .serializers import ( 
    GenreSerializer, 
    ThemeSerializer, 
    CountrySerializer, 
    LanguageSerializer, 
    StudioSerializer,
    FilmListSerializer,
    FilmDetailSerializer,
    FilmCreateUpdateSerializer
)

# 1. Genre views
class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['name']              # filter by name
    ordering_fields = ['id', 'name']         # allow ordering by id or name
    search_fields = ['name', 'description']  # search by name/description
    ordering = ['id']                        # default ordering

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]
    
# 2. Theme views
class ThemeListCreateView(generics.ListCreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['name']              # filter by name
    ordering_fields = ['id', 'name']         # allow ordering by id or name
    search_fields = ['name', 'description']  # search by name/description
    ordering = ['id']                        # default ordering

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]

class ThemeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]
    
# 3. Country views
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['name', 'code']         # filter by name
    ordering_fields = ['id', 'name', 'code']    # allow ordering by id or name
    search_fields = ['name', 'code']            # search by name/code
    ordering = ['id']                           # default ordering

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]

class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]

# 4. Language views
class LanguageListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['name', 'code']         # filter by name
    ordering_fields = ['id', 'name', 'code']    # allow ordering by id or name
    search_fields = ['name', 'code']            # search by name/code
    ordering = ['id']                           # default ordering

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]

class LanguageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]

# 5. Studio views
class StudioListCreateView(generics.ListCreateAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['name', 'founded_year', 'country']          # filter by name
    ordering_fields = ['id', 'name', 'founded_year', 'country']     # allow ordering by id/name/founded_year/country
    search_fields = ['name', 'description']                         # search by name/description
    ordering = ['id']                                               # default ordering

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]

class StudioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]
    
# 6. Film views
class FilmListCreateView(generics.ListCreateAPIView):
    queryset = Film.objects.all().order_by('id')
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    # Filter by year, title, genres, etc.
    filterset_fields = ['year', 'genres', 'themes', 'studios', 'countries', 'languages']
    ordering_fields = ['id', 'year', 'title', 'duration']
    search_fields = ['title', 'original_title', 'tagline', 'description']
    ordering = ['id']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FilmCreateUpdateSerializer
        return FilmListSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]

class FilmRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return FilmCreateUpdateSerializer
        return FilmDetailSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsRoleAdminOrStaff()]
        return [permissions.AllowAny()]