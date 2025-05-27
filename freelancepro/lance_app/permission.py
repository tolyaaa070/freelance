from rest_framework import permissions
class CheckRole(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'client':
            return True
        return False

class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
class CheckRoleReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'freelance':
            return False
        return True
class CheckOffer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'freelance':
            return True
        return False
