from django.db import models

# Create your models here.

from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=250)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации')  # ← УБРАТЬ auto_now_add=True
    name = models.CharField('Автор', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name_plural = 'Статьи'


