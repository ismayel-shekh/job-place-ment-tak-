from rest_framework import generics
from rest_framework import viewsets
from .models import Recipe, Ingredient, Rating, Comment
from .serializers import RecipeSerializer, IngredientSerializer, RatingSerializer, CommentSerializer

class RecipeListCreateAPIView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientListCreateAPIView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

