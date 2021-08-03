from rest_framework import serializers
from .models import Profile
from games.models import Game
from games.serializers import GameSummarySerializer
from discs.serializers import UserDiscSerializer


class ProfileSerializer(serializers.ModelSerializer):
   last_game = GameSummarySerializer(source='get_last_game')
   disc_bag = UserDiscSerializer(many=True)
   class Meta:
      model = Profile
      fields = '__all__'