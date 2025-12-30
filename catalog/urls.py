from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import (MainTemplateView, ContactsTemplateView, CatalogsTemplateView, CategoryListView, ProductListView,
                           ProductDetailView)


app_name = CatalogConfig.name


urlpatterns = [
    path("", MainTemplateView.as_view(), name="main"),
    path("home/", MainTemplateView.as_view(), name="main"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("catalogs/", CatalogsTemplateView.as_view(), name="catalogs"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("categories/<int:category_id>/", ProductListView.as_view(), name="product_list"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),

]