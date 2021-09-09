from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import DiscViewSet, UserDiscViewSet, DiscSearchViewSet, RelatedDiscViewSet


router = routers.DefaultRouter()
router.register(r'list', DiscViewSet)
router.register(r'user-discs', UserDiscViewSet, basename='user discs')
router.register(r'search', DiscSearchViewSet, basename='disc search')
router.register(r'related-discs', RelatedDiscViewSet, basename='related discs')

urlpatterns = [
   path('', include(router.urls)),
]

