from django.urls import path,include
from bookings import views

urlpatterns = [
    path('',views.index),
    path('<int:pk>/<str:location>/',views.index)
]