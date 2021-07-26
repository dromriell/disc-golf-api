from rest_framework import serializers
from .models import Profile
from games.models import Game
from games.serializers import GameSummarySerializer


class ProfileSerializer(serializers.ModelSerializer):
   last_game = GameSummarySerializer(source='get_last_game')
   class Meta:
      model = Profile
      fields = '__all__'