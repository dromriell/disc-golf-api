from rest_framework import serializers
from .models import Disc

class DiscSerializer(serializers.ModelSerializer):
   class Meta:
      model = Disc
      fields = '__all__'


