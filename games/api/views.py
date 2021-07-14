from rest_framework.viewsets import ModelViewSet
from ..models import Game, ScoreCard, HoleScore, Stroke
from ..serializers import (
   GameSerializer,
   ScoreCardSerializer,
   HoleScoreSerializer,
   StrokeSerializer
   )


class GameViewSet(ModelViewSet):
   queryset = Game.objects.all()
   serializer_class = GameSerializer

