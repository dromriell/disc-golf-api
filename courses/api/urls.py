from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import CourseViewSet, HoleViewSet


router = routers.DefaultRouter()
router.register(r'list', CourseViewSet)
router.register(r'holes', HoleViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
