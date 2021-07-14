from courses.models import Hole
from django.db import models
from rest_framework import serializers
from .models import Game, ScoreCard, HoleScore, Stroke

class StrokeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Stroke
      fields = '__all__'


class HoleScoreSerializer(serializers.ModelSerializer):
   class Meta:
      model = HoleScore
      fields = '__all__'


class ScoreCardSerializer(serializers.ModelSerializer):
   class Meta:
      model = ScoreCard
      fields = '__all__'


class GameStrokeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Stroke
      fields = '__all__'

   def to_representation(self, data):
      updated_data = super().to_representation(data)
      updated_data['position'] = data.parse_coordinates(data.position)
      return updated_data


class GameHoleScoreSerializer(serializers.ModelSerializer):
   strokes = GameStrokeSerializer(many=True)
   class Meta:
      model = HoleScore
      fields = ('score', 'hole', 'strokes')


class GameScoreCardSerializer(serializers.ModelSerializer):
   scores = GameHoleScoreSerializer(many=True)

   class Meta:
      model = ScoreCard
      fields = ('player', 'total_score', 'scores')


class GameSerializer(serializers.ModelSerializer):
   # holes = HoleSerializer(source='hole_set', many=True, read_only=True)
   players = GameScoreCardSerializer(source='scorecards', many=True)
   
   class Meta:
      model = Game
      fields = '__all__'
