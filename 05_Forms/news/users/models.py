from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True)
    phone = models.IntegerField(unique=True, null=True, blank=True)
    date_of_birth = models.DateField(blank=True)
    discount_card = models.IntegerField(unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    news_count = models.IntegerField(default=0)
