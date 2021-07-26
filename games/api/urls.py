from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import GameViewSet, ScoreCardViewSet, HoleScoreViewSet, GameSummaryViewSet


router = routers.DefaultRouter()
router.register(r'list', GameViewSet)
router.register(r'scorecards', ScoreCardViewSet, basename='scorecards')
router.register(r'hole_scores', HoleScoreViewSet, basename='hole_scores')
router.register(r'game-summary', GameSummaryViewSet, basename='game_summary')

urlpatterns = [
   path('', include(router.urls)),
]