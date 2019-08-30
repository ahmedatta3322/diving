from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('diver/<int:id>/',views.id),
    path('<str:searchq>/',views.search),
]