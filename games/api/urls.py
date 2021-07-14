from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import GameViewSet, ScoreCardViewSet, HoleScoreViewSet


router = routers.DefaultRouter()
router.register(r'list', GameViewSet)
router.register(r'scorecards', ScoreCardViewSet, basename='scorecards')
router.register(r'hole_scores', HoleScoreViewSet, basename='hole_scores')

urlpatterns = [
   path('', include(router.urls)),
]