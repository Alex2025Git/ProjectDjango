from catalog.models import Category, Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_category_from_cache():
    """Получение данные о категориях из кэш, если кэш пуст, получает данные из БД"""

    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "category_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories


def get_product_list_from_cache(category_id):
    """Получение данные о продуктах в выбранной катеогории, если кэш пуст, получает данные из БД"""

    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)
    key = f'product_list_{category_id}'
    queryset = cache.get(key)
    if queryset is not None:
        return queryset
    queryset = Product.objects.filter(category_id=category_id)
    cache.set(key, queryset)
    return queryset


def get_product_from_cache(pk):
    """Получение данные о выбранном продукте из кэш, если кэш пуст, получает данные из БД"""

    if not CACHE_ENABLED:
        return Product.objects.filter(pk=pk)
    key = f'product_{pk}'
    queryset = cache.get(key)
    if queryset is not None:
        return queryset
    queryset = Product.objects.filter(pk=pk)
    cache.set(key, queryset)
    return queryset