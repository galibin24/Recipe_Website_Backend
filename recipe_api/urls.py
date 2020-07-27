from django.urls import path

from . import views

urlpatterns = [
    path("recipes/", views.RecipeList.as_view()),
    path("recipes/<int:pk>", views.RecipeItem.as_view()),
]
