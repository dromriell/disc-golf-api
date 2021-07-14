from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import DiscViewSet


router = routers.DefaultRouter()
router.register(r'list', DiscViewSet)

urlpatterns = [
   path('', include(router.urls)),
]

