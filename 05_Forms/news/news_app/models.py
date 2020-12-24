from django.contrib.auth.models import User
from django.db import models

from .utils import slugify


class News(models.Model):
    name = models.CharField(max_length=1000, db_index=True, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст новости')
    tags = models.ManyToManyField('NewsTags', blank=True, db_index=True, related_name='news')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(verbose_name='Активно', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class NewsComments(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=20, blank=True, verbose_name='Пользователь')
    comment_text = models.TextField(blank=False, verbose_name='Текст комментария')
    news = models.ForeignKey('News', related_name='comments', on_delete=models.CASCADE, verbose_name='К новости')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class NewsTags(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug:
            super(NewsTags, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.name)
            super(NewsTags, self).save(*args, **kwargs)