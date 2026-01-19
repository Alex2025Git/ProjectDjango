from enum import nonmember
from idlelib.configdialog import is_int

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
    elif ('register' in path or 'login' in path) and item in 'login':
        return 'active aria-current="page" style="background-color: #0d6efd;border-radius: 0.5rem"'
    else:
        return 'text-white'


@register.filter
def get_heading(path, item=None):
    if 'category' in path:
        return 'Категории'
    if 'categories' in path:
        category_id = path.split('/')[2]
        return Category.objects.get(id=category_id).name
    if 'products' in path:
        product_id = path.split('/')[2]
        if product_id.isdigit() :
            return Product.objects.get(id=product_id).name
        return 'Главная'
    elif 'catalogs' in path:
        return 'Заказы'
    elif 'contacts' in path:
        return 'Контакты'
    elif 'blogs' in path:
        return 'B L O G'
    elif 'login' in path:
        referer = item.headers._store.get('referer')
        if referer:
            if 'register' in referer[1]:
                return 'Подтвердите регистрацию, уведомление направлено по почте.'
            elif 'categories' in referer[1]:
                return 'Для просмотра информации по товарам "Войдите или Зарегистрируйтесь"'
            else:
                'Добро пожаловать!'
        else:
            return 'Учетная запись подтверждена, пройдите авторизацию'
        return 'Добро пожаловать!'
    elif 'register' in path:
        return 'Регистрация'
    elif 'profile' in path:
        return 'Профиль'
    else:
        return 'Главная'


@register.filter
def get_referer(path):
    if 'categories' in path._store.get('referer')[1]:
        return f"/categories/{path._store.get('referer')[1].split('/')[4]}"
    return '/category'
