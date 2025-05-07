from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



# Create your models here.
class MyUser(AbstractUser):
    first_name = None
    last_name = None
    username = None

    groups = models.ManyToManyField(Group, blank=True, related_name='myuser_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='myuser_permissions')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    is_customer = models.BooleanField(default=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save()

    USERNAME_FIELD = 'phone'

    def __str__(self):
        return str(self.id)


class OrganizationSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='organization_logos/', blank=True, null=True)  
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)  
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_categories/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    food_type_choices = [
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_items/', blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    food_type = models.CharField(max_length=255, choices=food_type_choices, blank=True, null=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='foods', null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='foods', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


# class Customer(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
#     password = models.CharField(max_length=500, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to='customers/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

#     def __str__(self):
#         return self.name
    
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.password = make_password(self.password)
#         super().save()


class Order(models.Model):
    status_choices = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, choices=status_choices, default='Pending')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user.name + " - " + str(self.id)


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.food.name + " - " + str(self.order.id) + " - " + str(self.quantity)

class Banner(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/', blank=True, null=True) 
    url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Rating(models.Model):
    id = models.BigAutoField(primary_key=True)
    star = models.IntegerField(default=0)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ratings', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.star) + " - " + self.food.name + " - " + self.user.name