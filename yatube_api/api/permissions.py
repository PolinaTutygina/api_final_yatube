from rest_framework import permissions


class ReadOnlyOrIsAuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAuthenticatedForFollow(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated


class CommentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
