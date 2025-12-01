from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import main, contacts, catalogs, category

app_name = CatalogConfig.name


urlpatterns = [
    path("", main, name="main"),
    path("home/", main, name="main"),
    path("contacts/", contacts, name="contacts"),
    path("catalogs/", catalogs, name="catalogs"),
    path("category/", category, name="category"),
]
