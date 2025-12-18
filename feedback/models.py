from django.db import models

# Create your models here.
# feedback/models.py или main/models.py
from django.db import models


class Feedback(models.Model):
    CATEGORY_CHOICES = [
        ('question', 'Вопрос'),
        ('suggestion', 'Предложение'),
        ('complaint', 'Жалоба'),
        ('cooperation', 'Сотрудничество'),
        ('other', 'Другое'),
    ]

    STATUS_CHOICES = [
        ('new', 'Новое'),
        ('in_progress', 'В обработке'),
        ('resolved', 'Решено'),
        ('closed', 'Закрыто'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='question', verbose_name='Категория')
    message = models.TextField(verbose_name='Сообщение')
    rating = models.PositiveSmallIntegerField(default=0, verbose_name='Оценка (1-5)')
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name='IP адрес')
    user_agent = models.TextField(blank=True, verbose_name='User Agent')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%d.%m.%Y')})"