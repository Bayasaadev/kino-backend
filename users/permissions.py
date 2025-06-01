from rest_framework import permissions

class IsRoleAdmin(permissions.BasePermission):
    """
    Allows access only to users with role='admin'
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')

class IsRoleStaff(permissions.BasePermission):
    """
    Allows access only to users with role='staff'
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'staff')
    
class IsRoleAdminOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role in ('admin', 'staff')
        )
