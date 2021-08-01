from users.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from ..serializers import UserSerializer

USER = get_user_model()

class UserViewSet(ModelViewSet):

   queryset = USER.objects.all()
   serializer_class = UserSerializer

