from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
   RetrieveModelMixin,
   UpdateModelMixin,
   DestroyModelMixin,
   CreateModelMixin
)
from django.contrib.auth import get_user_model

from ..serializers import UserSerializer

USER = get_user_model()

class UserViewSet(RetrieveModelMixin, 
   UpdateModelMixin, 
   DestroyModelMixin, 
   CreateModelMixin, 
   GenericViewSet):

   queryset = USER.objects.all()
   serializer_class = UserSerializer
