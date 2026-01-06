from django.db import models

class BlogRecord(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(null=True, blank=True, upload_to="blog/photos", verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=False, verbose_name='Публикуется')
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "BlogRecord"
        verbose_name_plural = "BlogRecords"
        ordering = ['created_at']
