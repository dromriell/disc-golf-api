from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from ..models import Game, ScoreCard, HoleScore, Stroke
from ..serializers import (
   GameSerializer,
   ScoreCardSerializer,
   GameHoleScoreSerializer,
   GameSummarySerializer
   )


USER = get_user_model()


class GameViewSet(ModelViewSet):
   authentication_classes = [TokenAuthentication, SessionAuthentication]
   permission_classes = [IsAuthenticated]

   queryset = Game.objects.all()
   serializer_class = GameSerializer


class ScoreCardViewSet(ModelViewSet):
   authentication_classes = [TokenAuthentication, SessionAuthentication]
   permission_classes = [IsAuthenticated]

   serializer_class = ScoreCardSerializer

   def get_queryset(self):
      req_user = self.request.user
      spec_user = self.request.query_params.get('user', None)

      if spec_user:
         USER.objects.get(id=spec_user)
         return ScoreCard.objects.filter(player=spec_user)
   
      return ScoreCard.objects.filter(player=req_user)


class HoleScoreViewSet(ModelViewSet):
   authentication_classes = [TokenAuthentication, SessionAuthentication]
   permission_classes = [IsAuthenticated]

   serializer_class = GameHoleScoreSerializer

   def get_queryset(self):
      req_user = self.request.user
      spec_user = self.request.query_params.get('user', None)

      if spec_user:
         USER.objects.get(id=spec_user)
         return HoleScore.objects.filter(score_card__player=spec_user)
   
      return HoleScore.objects.filter(score_card__player=req_user)


class GameSummaryViewSet(ModelViewSet):
   authentication_classes = [TokenAuthentication, SessionAuthentication]
   permission_classes = [IsAuthenticated]

   serializer_class = GameSummarySerializer

   def get_queryset(self):
      req_user = self.request.user
      spec_user = self.request.query_params.get('user', None)

      if spec_user:
         USER.objects.get(id=spec_user)
         return ScoreCard.objects.filter(player=spec_user)[:5]
   
      return ScoreCard.objects.filter(player=req_user.id)[:5]

