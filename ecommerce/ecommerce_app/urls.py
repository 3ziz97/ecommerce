from django.urls import path
from .views import *
app_name = "ecommerce_app"

urlpatterns =[
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contactus/", ContactView.as_view(), name="contactus"),
]