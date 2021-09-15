from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user

class IsAuthorOrReceiver(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.receiver == request.user or obj.sender == request.user