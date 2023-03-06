from django.urls import path
from .views import *
app_name = "ecommerce_app"

urlpatterns =[
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("all_products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    #path("brands/", BrandView.as_view(), name="brands"),
]