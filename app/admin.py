from django.contrib import admin
from app.models import (Banner, MyUser, Food, FoodCategory, Order, OrderItem,
    OrganizationSetting, Rating, Restaurant)

# Register your models here.
@admin.register(MyUser)
class MyUser(admin.ModelAdmin):
    list_display = ('id', 'phone', 'is_customer', 'is_superuser')
    search_fields = ('phone', 'is_customer', 'is_superuser')
    list_filter = ('phone', 'is_customer', 'is_superuser')


@admin.register(OrganizationSetting)
class OrganizationSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'address', 'phone', 'email')
    search_fields = ('name','address','email')
    list_filter = ('name','address')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'address', 'phone')
    search_fields = ('name','address', 'phone')
    list_filter = ('name','address', 'phone')


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'price', 'discount', 'food_type', 'category', 'restaurant')
    search_fields = ('name','price','discount','food_type')
    list_filter = ('name','price','discount','food_type', 'category', 'restaurant')


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'phone','address')
#     search_fields = ('name','phone','address')
#     list_filter = ('name','phone','address')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'food', 'user', 'star')
    search_fields = ('food','user','star')
    list_filter = ('food','user','star')



class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'user', 'address', 'total', 'status')
    search_fields = ('user', 'address', 'total','status')
    list_filter = ('user', 'address', 'total','status')