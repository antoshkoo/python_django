from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    ACTIVE_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )
    name = models.CharField(max_length=1000, db_index=True, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.IntegerField(verbose_name='Активно', choices=ACTIVE_CHOICES, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class NewsComments(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=20, blank=True, verbose_name='Пользователь')
    comment_text = models.TextField(blank=False, verbose_name='Текст комментария')
    news = models.ForeignKey('News', related_name='comments', on_delete=models.CASCADE, verbose_name='К новости')
