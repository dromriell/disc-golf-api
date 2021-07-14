from rest_framework.viewsets import ModelViewSet
from ..models import Course, Hole
from ..serializers import CourseSerializer, HoleSerializer


class CourseViewSet(ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer

class HoleViewSet(ModelViewSet):
   queryset = Hole.objects.all()
   serializer_class = HoleSerializer