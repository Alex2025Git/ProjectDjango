import time

from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, View, TemplateView
from unicodedata import category

from catalog.models import Product,Category


class MainTemplateView(TemplateView):
    template_name = "catalog/main.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    # if request.method == "POST":
    #     name = request.POST["name"]
    #     email = request.POST["email"]
    #     message = request.POST["messageInput"]
    #     time.sleep(2)
    # return render(request, "catalog/contacts.html")


class CatalogsTemplateView(TemplateView):
    template_name = "catalog/catalogs.html"


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs.get("category_id"))


class ProductDetailView(DetailView):
    model = Product
