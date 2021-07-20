from rest_framework import serializers
from .models import Profile
from games.models import Game
from games.serializers import LastGameSummarySerializer


class ProfileSerializer(serializers.ModelSerializer):
   last_game = LastGameSummarySerializer(source='get_last_game')
   class Meta:
      model = Profile
      fields = '__all__'