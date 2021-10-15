from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

USER = get_user_model()

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = USER
      fields = '__all__'

   def create(self, validated_data):
    password = validated_data.pop('password')
    user = super().create(validated_data)
    user.set_password(password)
    user.save()
    Token.objects.get_or_create(user=user)
    return user

class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model = USER
      fields = ['id', 'last_login', 'first_name', 'last_name', 'email', 'birth_day', 'state', 'username']