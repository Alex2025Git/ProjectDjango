import os

from django.forms import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product

FILTER_WORLD = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно',
                'радар']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('owner',)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть "Отрицательной"')
        return price

    def clean_photo(self):
        photo = self.cleaned_data['photo']
        if photo is not None:
            size_in_bytes = photo.size
            extension = os.path.splitext(photo.name)[1].lower()  # Преобразование в нижний регистр
            if extension not in ('.jpg', '.jpeg', '.png'):
                raise ValidationError("Загрузка возможна фйалов с расширением: '.jpg', '.jpeg', '.png'")
            if size_in_bytes > 5242880:
                raise ValidationError("Размер файла не может превышать 5Мб")

    def clean_category(self):
        category = self.cleaned_data['category']
        if category is None:
            raise ValidationError("Укажите категорию продукта")
        return category


    def clean(self):
        cleaned_data = super().clean()
        words = []
        filter_words = FILTER_WORLD
        product_name = cleaned_data.get("name")
        product_description = cleaned_data.get("description")
        words.append(product_name)
        words.append(product_description)

        for word in words:
            for filter_word in filter_words:
                if filter_word in word.lower():
                    if words.index(word) == 0:
                        find_word = 'name'
                    else:
                        find_word = 'description'
                    self.add_error(find_word,
                                   f'Указанное слово "{filter_word}" не может быть использовано в "{find_word}"')


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = 'is_published',
