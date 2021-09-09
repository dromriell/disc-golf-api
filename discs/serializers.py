import json
from rest_framework import serializers
from .models import Disc, UserDisc, Manufacturer
from profiles.models import Profile


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

   def to_internal_value(self, data):
       print(data)
       profile = Profile.objects.get(id=data['profile'])
       disc = Disc.objects.get(id=data['disc'])
       parsed_data = {'profile': profile, 'disc': disc}
       return(parsed_data)

