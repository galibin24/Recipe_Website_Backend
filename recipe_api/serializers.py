from recipe_api.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    Title = serializers.CharField(required=True)
    Description = serializers.CharField(required=True)
    imageUrl = serializers.CharField(required=False, default="")

    class Meta:
        model = Recipe
        fields = ["id", "Title", "Description", "imageUrl"]

