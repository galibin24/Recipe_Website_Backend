from recipe_api.models import Recipe
from rest_framework import serializers
from django.core import serializers as django_serializers


class RecipeSerializer(serializers.ModelSerializer):
    Title = serializers.CharField(required=True)
    Description = serializers.CharField(required=True)
    imageUrl = serializers.CharField(required=False, default="")
    recipe_type = serializers.CharField( required=False)
    preperation_minutes = serializers.IntegerField(required=False, default=60)

    owner = serializers.ReadOnlyField(source="owner.username")

    def to_representation(self, instance):
        return {
            'Title': instance.Title,
            "Description": instance.Description,
            "imageUrl": instance.imageUrl,
            "recipe_type": instance.get_recipe_type_display(),
            "preperation_minutes": instance.preperation_minutes,
            "owner": instance.owner.username,
            "id": instance.id
        }
   
    class Meta:
        model = Recipe
        fields =  '__all__' 
        

       
   

