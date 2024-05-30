from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()
router.register('recipes', views.RecipeListCreateAPIView)
router.register('ingredients', views.IngredientListCreateAPIView)
router.register('ratings', views.RatingListCreateAPIView)
router.register('comments', views.CommentListCreateAPIView)
urlpatterns = [
    path('', include(router.urls))
]
