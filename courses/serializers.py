from rest_framework import serializers
from .models import Course, Hole

class HoleSerializer(serializers.ModelSerializer):
   class Meta:
      model = Hole
      fields = '__all__'

   def to_representation(self, data):
      updated_data = super().to_representation(data)
      updated_data['center'] = data.parse_coordinates(data.center)
      updated_data['tee_box'] = data.parse_coordinates(data.tee_box)
      updated_data['basket'] = data.parse_coordinates(data.basket)
      return updated_data


class CourseSerializer(serializers.ModelSerializer):
   holes = HoleSerializer(source='hole_set', many=True, read_only=True)
   
   class Meta:
      model = Course
      fields = '__all__'


class CourseSummarySerializer(serializers.ModelSerializer):
   class Meta:
      model = Course
      fields = '__all__'

