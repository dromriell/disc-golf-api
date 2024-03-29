"""DG_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import PDGAPIView
from users.views import CustomObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/discs/', include('discs.api.urls')),
    path('api/v1/courses/', include('courses.api.urls')),
    path('api/v1/profiles/', include('profiles.api.urls')),
    path('api/v1/games/', include('games.api.urls')),
    path('api/v1/users/', include('users.api.urls')),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api-token-auth'),
    path('api-pdga/auth/', PDGAPIView.as_view(), name='pdga-auth'),
]
