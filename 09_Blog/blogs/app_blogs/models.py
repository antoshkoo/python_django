import os

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
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

    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super().delete(*args, **kwargs)


@receiver(models.signals.post_delete, sender=Gallery)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Gallery)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Gallery.objects.get(pk=instance.pk).image
    except Gallery.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
