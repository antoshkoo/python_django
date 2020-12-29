from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='О себе', blank=True)
    avatar = models.FileField(upload_to='images/avatar/', blank=True, null=True, verbose_name='Аватар')
