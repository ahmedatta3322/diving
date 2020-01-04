from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("register/",views.register),
    path("create/",views.create),
    path("view/",views.view)
    
]

