from rest_framework.viewsets import ModelViewSet
from ..models import Disc
from ..serializers import DiscSerializer

class DiscViewSet(ModelViewSet):
   queryset = Disc.objects.all()
   serializer_class = DiscSerializer
