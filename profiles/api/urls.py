from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import ProfileViewSet


router = routers.DefaultRouter()
router.register(r'list', ProfileViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
