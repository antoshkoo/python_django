from django.db import models


class News(models.Model):
    ACTIVE_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )
    name = models.CharField(max_length=1000, db_index=True, verbose_name='news')
    body = models.TextField(verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.IntegerField(verbose_name='Активно', choices=ACTIVE_CHOICES, default=1)

    def __str__(self):
        return self.name


class NewsComments(models.Model):
    user_name = models.CharField(max_length=20, blank=False, verbose_name='Пользователь')
    comment_text = models.TextField(blank=False, verbose_name='Текст комментария')
    news = models.ForeignKey('News', on_delete=models.CASCADE)

# Создайте новостной сайт. Он должен уметь отображать новости и поддерживать возможность их комментировать.
# Создайте модель Новость с полями: название, содержание, дата создания, дата редактирования, флаг активности.
# Создайте модель Комментарий с полями: имя пользователя, текст комментария, новость (связь с моделью новость).
