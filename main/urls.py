from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),    
    path('home/', views.home, name="home"),
    path('usstockpick/', views.usstockpick, name="usstockpick"),
    path('about/', views.about, name="about"),
]
