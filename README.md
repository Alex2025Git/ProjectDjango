# Проект "Интернет-магазин" на Django
Проект находится в разработке.


## Содержание
- [Технологии](#технологии)
- [Описание структуры проекта](#описание)
- [Тестирование](#тестирование)


## Технологии

- Python 3.13
- Виртуальное окружение Poetry
- Работа с Git
- Django


## Описание

Реализовано шаблоны и добавлены контроллеры для отображения страниц:

- Главная   ([main.html](catalog/templates/main.html))
- Категории ([category.html](catalog/templates/category.html))
- Заказы    ([catalogs.html](catalog/templates/catalogs.html))
- Контакты  ([contacts.html](catalog/templates/contacts.html))

Добавлена обработка данных в форме - Контакты  ([contacts.html](catalog/templates/contacts.html))

Структура проета состоит из:

- Проект Django
  
  - Приложения:
    - [catalog](catalog)
        - [management](catalog/management)
          - [commands](catalog/management/commands) 
        - [migrations](catalog/migrations)
        - [templates](catalog/templates)
        - [admin.py](catalog/admin.py)
        - [apps.py](catalog/apps.py)
        - [models.py](catalog/models.py)
        - [tests.py](catalog/tests.py)
        - [urls.py](catalog/urls.py)
        - [views.py](catalog/views.py)
        - [media](media)
      
- [requirements.txt](requirements.txt)
- [README.md](README.md)


## Тестирование
...
