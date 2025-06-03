from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    RegisterSerializer, 
    UserPublicSerializer, 
    UserPrivateSerializer,
    UserEditProfileSerializer, 
    UserRoleUpdateSerializer, 
    AdminTokenObtainPairSerializer
)
from .permissions import IsRoleAdmin, IsRoleAdminOrStaff

User = get_user_model()

# 1. Register API
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# 2. Logout API
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# 3. User List API (public)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [permissions.AllowAny]

# 4. User Detail API (public)
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id' 

# 3.1. User List API (private)
class UserListPrivateView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPrivateSerializer
    permission_classes = [IsRoleAdminOrStaff]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['role']                     # filter by role
    ordering_fields = ['id', 'username', 'role']    # allow ordering by id/username/role
    search_fields = ['username', 'email']           # search by username/email
    ordering = ['id']                               # default ordering
    

# 4.1. User Detail API (private)
class UserDetailPrivateView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPrivateSerializer
    permission_classes = [IsRoleAdminOrStaff]
    lookup_field = 'id' 

# 5. Profile API (self only)
class ProfileMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserPrivateSerializer(request.user)
        return Response(serializer.data)

# 6. Edit Profile API (self only)
class EditProfileView(generics.UpdateAPIView):
    serializer_class = UserEditProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
# 7. Update User's Role (admin only)
class UpdateUserRoleView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleUpdateSerializer
    permission_classes = [IsRoleAdmin]
    lookup_field = 'id'

# 8. Follow
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, id):
    try:
        user_to_follow = User.objects.get(id=id)
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        user_to_follow.followers.add(request.user)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

# 9. Unfollow
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, id):
    try:
        user_to_unfollow = User.objects.get(id=id)
        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        user_to_unfollow.followers.remove(request.user)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
# 10. Followers
@api_view(['GET'])
@permission_classes([AllowAny])
def user_followers(request, id):
    """
    List all followers of the user with id=<id>
    """
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=404)
    followers = user.followers.all()
    serializer = UserPublicSerializer(followers, many=True, context={'request': request})
    return Response(serializer.data, status=200)

# 11. Following
@api_view(['GET'])
@permission_classes([AllowAny])
def user_following(request, id):
    """
    List all users the user with id=<id> is following
    """
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=404)
    following = user.following.all()
    serializer = UserPublicSerializer(following, many=True, context={'request': request})
    return Response(serializer.data, status=200)

# 12. Admin Login
class AdminTokenObtainPairView(TokenObtainPairView):
    serializer_class = AdminTokenObtainPairSerializer