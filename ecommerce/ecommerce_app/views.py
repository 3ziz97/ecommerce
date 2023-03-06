from django.shortcuts import render
from django.views.generic import  TemplateView
from .models import *
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context["product"] = Product.objects.all().order_by("-id")
        return context


class ProductView(TemplateView):
    template_name = "productdetail.html"

class AboutView(TemplateView):
    template_name = "about.html"


class AllProductsView(TemplateView):
    template_name = "allproducts.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allcategories"] = Category.objects.all()
        return context

class ProductDetailView(TemplateView):
    template_name = "productdetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        product = Product.objects.get(slug=url_slug)
        context['product'] = product
        return context

class AddToCartView(TemplateView):
    template_name = "addtocart.html"

#class BrandView(TemplateView):
    #template_name = "brands.html"