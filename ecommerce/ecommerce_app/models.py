from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    price = models.FloatField()
    sale_price = models.FloatField(null=True, blank=True)
    description = models.TextField()
    view_count = models.PositiveIntegerField(default=0) #(like IntegerField but only 0 and positive numbers over 0)

    def __str__(self):
        return self.title

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Cart: " + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + "CartProduct: " + str(self.id)

#class Brand(models.Model):
    #title = models.CharField(max_length=100)
    #slug = models.SlugField(unique=True)
    #link = models.CharField(max_length=300)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by =models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    total = models.FloatField()
    #order_status = models.CharField(max_length=50, choices=ORDER_STATUS)





