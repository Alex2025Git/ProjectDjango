
from django import template

from catalog.models import Category, Product

register = template.Library()


@register.filter
def media_filter(path):
    if path:
        return f'/media/{path}'
    return ''


@register.filter
def active_class(path, item):
    if ('base' in path or 'home' in path or path == '/') and  item  == '/':
        return 'active aria-current="page" style="background-color: #0d6efd;border-radius: 0.5rem"'
    elif 'catalogs' in path and item in 'catalogs':
        return 'active aria-current="page" style="background-color: #0d6efd;border-radius: 0.5rem"'
    elif 'contacts' in path and item in 'contacts':
        return 'active aria-current="page" style="background-color: #0d6efd;border-radius: 0.5rem"'
    elif ('category' in path or 'categories' in path or 'products'  in path) and item in 'category':
        return 'active aria-current="page" style="background-color: #0d6efd;border-radius: 0.5rem"'
    else:
        return 'text-white'


@register.filter
def get_heading(path):
    if 'category' in path:
        return 'Категории'
    if 'categories' in path:
        category_id = path.split('/')[2]
        return Category.objects.get(id=category_id).name
    if 'products' in path:
        product_id = path.split('/')[2]
        return Product.objects.get(id=product_id).name
    elif 'catalogs' in path:
        return 'Заказы'
    elif 'contacts' in path:
        return 'Контакты'
    elif 'blogs' in path:
        return 'B L O G'
    else:
        return 'Главная'
