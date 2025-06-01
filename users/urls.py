from django.urls import path
from .views import (
    RegisterView, 
    LogoutView,
    UserListView,
    UserDetailView,
    ProfileMeView,
    EditProfileView,
    UpdateUserRoleView,
    AdminTokenObtainPairView,
    follow_user,
    unfollow_user,
    user_followers,
    user_following
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', ProfileMeView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit-profile'),
    path('users/<int:id>/set-role/', UpdateUserRoleView.as_view(), name='update-user-role'),
    path('users/<int:id>/follow/', follow_user, name='user-follow'),
    path('users/<int:id>/unfollow/', unfollow_user, name='user-unfollow'),
    path('users/<int:id>/followers/', user_followers, name='user-followers'),
    path('users/<int:id>/following/', user_following, name='user-following'),
    path("admin-login/", AdminTokenObtainPairView.as_view(), name="admin-login"),
]
