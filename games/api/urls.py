from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import GameViewSet


router = routers.DefaultRouter()
router.register(r'list', GameViewSet)

urlpatterns = [
   path('', include(router.urls)),
]