"""diving URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from api import views
from frontend import urls
from django.conf.urls.static import static
from django.conf import settings
#router = routers.DefaultRouter()
#router.register('divers', divers) 
#path("divers/" , include(router.urls))
urlpatterns = [
    path("divers/" , views.divers.as_view()),
    path("courses/", views.courses.as_view()),
    path("",include('frontend.urls')),
    path("admin" , admin.site.urls)
    
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
