from rest_framework import serializers
from .models import Disc, UserDisc

class DiscSerializer(serializers.ModelSerializer):
   class Meta:
      model = Disc
      fields = '__all__'


class UserDiscSerializer(serializers.ModelSerializer):
   disc = DiscSerializer()
   class Meta:
      model = UserDisc
      fields = '__all__'


