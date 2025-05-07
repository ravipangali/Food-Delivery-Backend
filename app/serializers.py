from app.models import (Banner, MyUser, Food, FoodCategory, Order, OrderItem,
    OrganizationSetting, Rating, Restaurant)
from rest_framework import serializers


class OrganizationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationSetting
        depth = 10
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        depth = 10
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True).data
    class Meta:
        model = Food
        depth = 10
        fields = ('id', 'name', 'image', 'price', 'discount', 'food_type', 'category', 'restaurant', 'ratings')

class FoodCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True).data
    class Meta:
        model = FoodCategory
        depth = 10
        fields = ('id', 'name', 'image', 'foods')

class RestaurantSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True).data
    class Meta:
        model = Restaurant
        depth = 10
        fields = ('id', 'name', 'logo', 'address', 'phone', 'foods')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        depth = 10
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True).data
    class Meta:
        model = Order
        depth = 10
        fields = ('id', 'status', 'customer', 'address', 'latitude', 'longitude', 'phone', 'sub_total', 'delivery_charge', 'total', 'note', 'created_at', 'order_items')

class MyUserSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True).data
    class Meta:
        model = MyUser
        depth = 10
        fields = ('id', 'name', 'phone', 'address', 'image', 'orders')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        depth = 10
        fields = '__all__'