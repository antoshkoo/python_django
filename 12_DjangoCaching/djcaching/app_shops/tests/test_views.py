from django.contrib.auth.models import User
from django.test import TestCase

# balance - 10.0
from django.urls import reverse

USER_DATA = {
    'username': 'test',
    'password': 'test',
}

# balance - 460.0
USER_DATA_BOSS = {
    'username': 'test2',
    'password': 'test2',
}


class MainPageViewTest(TestCase):
    fixtures = ['users_data.json', 'profile_data.json', 'shops_data.json']

    def test_user_main_page(self):
        response = self.client.get(reverse('main_page_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertTrue('shops' in response.context)
        self.assertContains(response, '<h1>Loyalty program</h1>')
        self.assertContains(response, 'Sign in</a>')
        self.assertContains(response, 'Sign up</a>')
        self.assertContains(response, 'Traektoria')

    def test_logged_user_main_page(self):
        self.client.login(username=USER_DATA_BOSS['username'], password=USER_DATA_BOSS['password'])
        response = self.client.get(reverse('main_page_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertTrue('shops' in response.context)
        self.assertNotContains(response, 'Sign in</a>')
        self.assertContains(response, '<h1>Loyalty program</h1>')
        self.assertContains(response, 'Traektoria')
        self.assertContains(response, '<h5>Special offer</h5>')
        self.assertContains(response, '<li>Free shipping for orders 400+</li>')
        self.assertContains(response, '<p>Balance: 460.0$</p>')


class BuyViewTest(TestCase):
    fixtures = ['users_data.json', 'profile_data.json', 'shops_data.json']

    def test_logged_user_no_balance_buy_view(self):
        self.client.login(username=USER_DATA['username'], password=USER_DATA['password'])
        response = self.client.get(reverse('buy_url', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please charge your balance!')

    def test_logged_user_boss_balance_buy_view(self):
        self.client.login(username=USER_DATA_BOSS['username'], password=USER_DATA_BOSS['password'])
        response = self.client.get(reverse('buy_url', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you for order!')

        user = User.objects.get(username=USER_DATA_BOSS['username'])
        self.assertEqual(user.profile.balance, 430.0)
