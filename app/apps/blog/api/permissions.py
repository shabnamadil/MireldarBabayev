from rest_framework import permissions


class IsCommentAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Handle edit/delete operations
        elif obj.author == request.user:
            return True
