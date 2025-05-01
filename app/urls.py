from django.urls import path
from app import views

urlpatterns = [
    path('home', views.home),
    path('category/<str:id>', views.singleCategory),
]
