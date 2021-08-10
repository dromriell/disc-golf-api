import json
from rest_framework import serializers
from .models import Disc, UserDisc, Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
   class Meta:
      model = Manufacturer
      fields = '__all__'


class DiscSerializer(serializers.ModelSerializer):
   manufacturer = ManufacturerSerializer(read_only=True)
   type_display = serializers.CharField(source='get_type_display')
   class Meta:
      model = Disc
      fields = '__all__'


class UserDiscSerializer(serializers.ModelSerializer):
   disc = DiscSerializer()
   class Meta:
      model = UserDisc
      fields = '__all__'

