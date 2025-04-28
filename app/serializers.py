from app.models import (Banner, Customer, Food, FoodCategory, Order, OrderItem,
    OrganizationSetting, Rating, Restaurant)
from rest_framework import serializers


class OrganizationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationSetting
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True).data
    class Meta:
        model = Food
        fields = ('id', 'name', 'image', 'price', 'discount', 'food_type', 'category', 'restaurant', 'ratings')

class FoodCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True).data
    class Meta:
        model = FoodCategory
        fields = ('id', 'name', 'image', 'foods')

class RestaurantSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True).data
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'logo', 'address', 'phone', 'foods')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True).data
    class Meta:
        model = Order
        fields = ('id', 'status', 'customer', 'address', 'latitude', 'longitude', 'phone', 'sub_total', 'delivery_charge', 'total', 'note', 'created_at', 'order_items')

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True).data
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'address', 'image', 'orders')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'