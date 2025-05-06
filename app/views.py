from rest_framework.response import Response
from app.serializers import (BannerSerializer, FoodCategorySerializer, FoodSerializer,
    RestaurantSerializer)
from app.models import Banner, Food, FoodCategory, Restaurant
from django.db.models import Count, Prefetch
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Auth API
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return Response({'message': 'Login successful'}) 
    
    return Response({'message': 'Login failed'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    auth_logout(request)
    return Response({'message': 'Logout successful'})



# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    popular_items = Food.objects.annotate(
        order_count=Count('order_items')
    ).order_by('-order_count')


    data = {
        'banners': BannerSerializer(Banner.objects.order_by('-created_at'), many=True).data,
        'food_categories': FoodCategorySerializer(FoodCategory.objects.all(), many=True).data,
        'restaurants': RestaurantSerializer(Restaurant.objects.all(), many=True).data,
        'popular_items': FoodSerializer(popular_items, many=True).data
    }
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def singleCategory(request, id):
    data = {
        'category': FoodCategorySerializer(FoodCategory.objects.get(id=id), many=False).data,
    }
    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def singleRestaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)
    categories = FoodCategory.objects.filter(
        foods__restaurant=restaurant
        ).prefetch_related(
            Prefetch('foods', queryset=Food.objects.filter(restaurant=restaurant))
    ).distinct()
    
    data = {
        'restaurant': RestaurantSerializer(restaurant, many=False).data,
        'categories': FoodCategorySerializer(categories, many=True).data,
    }
    return Response(data)
