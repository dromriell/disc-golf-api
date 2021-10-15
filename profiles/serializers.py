from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model
from games.serializers import GameSummarySerializer
from discs.serializers import UserDiscSerializer
from users.serializers import UserProfileSerializer


USER = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
   last_game = GameSummarySerializer(source='get_last_game')
   user = UserProfileSerializer()
   disc_bag = UserDiscSerializer(many=True)
   class Meta:
      model = Profile
      fields = '__all__'
   def to_internal_value(self, data):
       parsed_data = { 
         "city": data['city'],
         "state": data['state'],
         'user': {
            "email": data['email'],
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "username": data['username'],
         }
         
      }
       return(parsed_data)

   def update(self, instance, validated_data):
      user = USER.objects.get(id=instance.user.id)
      user_data = validated_data['user']

      user.email = user_data['email']
      user.first_name = user_data['first_name']
      user.last_name = user_data['last_name']
      user.username = user_data['username']

      user.save()

      instance.city = validated_data['city']
      instance.state = validated_data['state']
      instance.save()
      instance.user = user

      return instance