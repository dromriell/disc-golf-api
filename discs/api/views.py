from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Disc, UserDisc
from ..serializers import DiscSerializer, UserDiscSerializer

class DiscViewSet(ModelViewSet):
   queryset = Disc.objects.all()
   serializer_class = DiscSerializer


class UserDiscViewSet(ModelViewSet):
   authentication_classes = [TokenAuthentication, SessionAuthentication]
   permission_classes = [IsAuthenticated]
   serializer_class = UserDiscSerializer

   def get_queryset(self):
      user = self.request.user
      queryset_all = UserDisc.objects.filter(profile=user.user_profile)

      return queryset_all


class DiscSearchViewSet(ModelViewSet):
   serializer_class = DiscSerializer

   def get_queryset(self):
      search_term = self.request.query_params.get('term', None)

      # Do not filter on queries less than two chars in length.
      if not search_term or len(search_term) < 2:
         return []
      # Check if term is wrapped in quotes and if so, filter by iexact
      if search_term[0] == '"' and search_term[-1] == '"':
         search_term = search_term[1:-1]
         print(search_term)
         queryset = Disc.objects.filter(name__iexact=search_term)
      # Otherwise filter by case insensitive icontains
      else:
         queryset = Disc.objects.filter(name__icontains=search_term)

      return queryset


class RelatedDiscViewSet(ModelViewSet):
   # Test viewset to find similar discs based on certain properties
   authentication_classes = [TokenAuthentication, SessionAuthentication]
   permission_classes = [IsAuthenticated]
   serializer_class = DiscSerializer

   def get_queryset(self):
      user = self.request.user
      weight = self.request.query_params.get('weight', None)
      diameter = self.request.query_params.get('diameter', None)
      height = self.request.query_params.get('height', None)
      rim_depth = self.request.query_params.get('rim_depth', None)
      inside_rim_diameter = self.request.query_params.get('inside_rim_diameter', None)
      rim_thickness = self.request.query_params.get('rim_thickness', None)
      rim_depth_to_diameter = self.request.query_params.get('rim_ratio', None)
      rim_configuration = self.request.query_params.get('rim_config', None)
      flexibility = self.request.query_params.get('flexibility', None)
      
      queryset = Disc.objects.filter(
         weight=weight
      ).filter(
         rim_depth_to_diameter=rim_depth_to_diameter
      ).filter(
         flexibility=flexibility
      )

      return queryset