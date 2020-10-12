from rest_framework import permissions
from recipe_api.models import Recipe

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            print(request.user)
            return True
        else:
            pk = int(request.path_info.split(r'/')[-1])
            obj = Recipe.objects.get(pk = pk)
            
            return obj.owner == request.user

