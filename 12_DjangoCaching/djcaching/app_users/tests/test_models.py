from django.contrib.auth.models import User
from django.test import TestCase

from app_users.models import Profile

LOAD_DATA = ['users_data.json', 'profile_data.json', 'shops_data.json']


class TestProfileModel(TestCase):
    fixtures = LOAD_DATA

    def test_profile_model(self):
        profile = Profile.objects.get(id=1)

        balance_label = profile._meta.get_field('balance').verbose_name
        self.assertEquals(balance_label, 'balance')

        user = User.objects.create_user(username='profile', password='profile')
        self.assertEquals(user.profile.balance, 0)
