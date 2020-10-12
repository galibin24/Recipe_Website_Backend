from rest_framework import serializers
from .models import CustomUser
from recipe_api.models import Recipe
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    # is it ok, do I even need it?
    recipes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Recipe.objects.all(), required = False
    )

    class Meta:
        model = CustomUser
        fields = ("id", "username", "password", "recipes")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        return data