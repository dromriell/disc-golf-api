import datetime
from discs.models import UserDisc
from courses.models import Hole
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from rest_framework import serializers
from .models import Game, ScoreCard, HoleScore, Stroke
from courses.models import Course, Hole
from courses.serializers import CourseSummarySerializer, HoleSerializer

USER = get_user_model()

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
   hole = HoleSerializer()
   class Meta:
      model = HoleScore
      fields = '__all__'

   def to_internal_value(self, data):
      internal_value_dict = {'strokes':[],}
      for key, value in data.items():
         if key == 'score_card':
            score_card = ScoreCard.objects.get(id=value)
            internal_value_dict[key] = score_card
            continue
         if key == 'hole':
            hole = Hole.objects.get(id=value)
            internal_value_dict['hole'] = hole
            continue
      for stroke in data['strokes']:
         if stroke['type'] == 'hole':
            is_hole = True
         else: is_hole = False
      
         internal_stroke = {
            'position': Point(stroke['lng'], stroke['lat'], srid=4326),
            'throw': stroke['throw'],
            'disc': UserDisc.objects.get(id=stroke['disc']),
            'dist': stroke['dist'],
            'isHole': is_hole
            }

         internal_value_dict['strokes'].append(internal_stroke)
      return internal_value_dict

   def create(self, validated_data):
      print(validated_data)
      strokes = validated_data.pop('strokes')
      new_hole_score = HoleScore.objects.create(**validated_data)
      for stroke in strokes:
         Stroke.objects.create(**stroke, hole_score=new_hole_score)
      print(new_hole_score)
      return new_hole_score


class GameScoreCardSerializer(serializers.ModelSerializer):
   scores = GameHoleScoreSerializer(many=True)

   class Meta:
      model = ScoreCard
      fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
   """
   Top level serializer for all game data. Will return all nested fields related to a
   given game. Created right after course is selected and will auto generate ScoreCard
   objects for all players included in the POST request body
   """
   players = GameScoreCardSerializer(source='scorecards', many=True, read_only=True)
   
   class Meta:
      model = Game
      fields = '__all__'
   
   def to_internal_value(self, data):
      # Return PATCH data with no additional processing
      if self.context['request'].method == 'PATCH':
         return data
      # Parse the request data and convert values to valid formats
      internal_value_dict = {}
      for key, value in data.items():
         if key == 'date':
            date = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
            internal_value_dict['date'] = date
            continue
         if key == 'course':
            course = Course.objects.get(id=value)
            internal_value_dict['course'] = course
            continue
         if key == 'players':
            players = []
            for player in value:
               print('PLAYER', player)
               players.append(USER.objects.get(id=player))
            internal_value_dict['players'] = players
      return internal_value_dict

   def create(self, validated_data):
      # Loop over players in data and generate new scorecards and
      # attach to a new Game object.
      players = validated_data.pop('players')
      new_game = Game.objects.create(**validated_data)
      for player in players:
         ScoreCard.objects.create(
            game=new_game, 
            player=player, 
            total_score=0
            )
      return new_game
      

class BasicGameSerializer(serializers.ModelSerializer):
   """
   Returns all model fields excluding the Many-to-One Scorecard field
   """
   course = CourseSummarySerializer(read_only=True)
   class Meta:
      model = Game
      fields = '__all__'

class GameSummarySerializer(serializers.ModelSerializer):
   """
   Serializer for returning a players last game summary. 
   Used with the ProfileSerializer 
   """
   game = BasicGameSerializer(read_only=True)
   class Meta:
      model = ScoreCard
      fields = '__all__'
