from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=120, db_index=True, verbose_name='Заголовок')
    body = models.TextField(db_index=True, verbose_name='Описание')
    files = models.FileField(upload_to='images/posts/%d-%m-%Y', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
