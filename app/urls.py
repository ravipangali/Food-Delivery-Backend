from django.urls import path
from app import views

urlpatterns = [
    # Auth Urls
    path('login', views.login),
    path('logout', views.logout),



    # Others
    path('home', views.home),
    path('category/<str:id>', views.singleCategory),
    path('restaurant/<str:id>', views.singleRestaurant),
]
