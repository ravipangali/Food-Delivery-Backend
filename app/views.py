from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import (BannerSerializer, FoodCategorySerializer, FoodSerializer,
    RestaurantSerializer)
from app.models import Banner, Food, FoodCategory, Restaurant
from django.db.models import Count

# Create your views here.
@api_view(['GET'])
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