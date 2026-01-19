from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (MainTemplateView, ContactsTemplateView, CatalogsTemplateView, CategoryListView, ProductListView,
                           ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView)


app_name = CatalogConfig.name


urlpatterns = [
    path("", MainTemplateView.as_view(), name="main"),
    path("home/", MainTemplateView.as_view(), name="main"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("catalogs/", CatalogsTemplateView.as_view(), name="catalogs"),
    path("category/", cache_page(60)(CategoryListView.as_view()), name="category_list"),
    path("categories/<int:category_id>/", cache_page(60)(ProductListView.as_view()), name="product_list"),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path('products/create/', ProductCreateView.as_view(), name="product_create"),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name="product_update"),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),


]