from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=120, db_index=True, verbose_name='Заголовок')
    body = models.TextField(db_index=True, verbose_name='Описание')
    pub_date = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.FileField(upload_to='images/posts/%d-%m-%Y')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='gallery')
