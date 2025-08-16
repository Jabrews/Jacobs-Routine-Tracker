from django.urls import path, re_path, include
from .import views

urlpatterns = [
    path('', views.HomeView, name='home' ),
    re_path(r"^(?:.*)/?$", views.HomeView),  
] 
