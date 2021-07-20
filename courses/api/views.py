from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import Course, Hole
from ..serializers import CourseSerializer, HoleSerializer


class CourseViewSet(ModelViewSet):
   authentication_classes = [TokenAuthentication, SessionAuthentication]
   permission_classes = [IsAuthenticated]

   queryset = Course.objects.all()
   serializer_class = CourseSerializer

class HoleViewSet(ModelViewSet):
   authentication_classes = [TokenAuthentication, SessionAuthentication]
   permission_classes = [IsAuthenticated]
   
   queryset = Hole.objects.all()
   serializer_class = HoleSerializer