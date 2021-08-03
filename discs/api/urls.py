from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import DiscViewSet, DiscSearchViewSet


router = routers.DefaultRouter()
router.register(r'list', DiscViewSet)
router.register(r'search', DiscSearchViewSet, basename='disc search')

urlpatterns = [
   path('', include(router.urls)),
]

