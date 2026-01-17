from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to="catalog/photos")
    is_published = models.BooleanField(default=False, verbose_name='Публикуется')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True, verbose_name="Владелец", help_text="Укажите владельца товара")


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["created_at"]
        permissions = [
            ('can_unpublish_product','can unpublish product')
        ]

    def __str__(self):
        return self.name
