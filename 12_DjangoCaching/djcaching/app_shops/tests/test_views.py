from django.contrib.auth.models import User
from django.test import TestCase

from django.urls import reverse

from app_shops.models import Good, Order

USER_DATA = {
    'username': 'test',
    'password': 'test',
}

USER_DATA_BOSS = {
    'username': 'test2',
    'password': 'test',
}


class MainPageViewTest(TestCase):
    fixtures = ['initial_data.json']

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
        self.assertContains(response, '<p>Balance: 460.0$</p>')


class BuyViewTest(TestCase):
    fixtures = ['initial_data.json']

    def test_logged_user_no_balance_buy_view(self):
        good = Good.objects.first()
        self.client.login(username=USER_DATA['username'], password=USER_DATA['password'])
        response = self.client.post(reverse('buy_url'), {'good_id': good.id, 'quantity': 100500})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please charge your balance!')

    def test_logged_user_boss_balance_buy_view(self):
        good = Good.objects.first()
        self.client.login(username=USER_DATA_BOSS['username'], password=USER_DATA_BOSS['password'])
        response = self.client.post(reverse('buy_url'), {'good_id': good.id, 'quantity': 1})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you for order!')


class RefuseViewTest(TestCase):
    fixtures = ['initial_data.json']

    def test_refuse_view(self):
        self.client.login(username=USER_DATA_BOSS['username'], password=USER_DATA_BOSS['password'])

        user = User.objects.get(username=USER_DATA_BOSS['username'])
        start_balance = user.profile.balance
        good = Good.objects.first()

        self.client.post(reverse('buy_url'), {'good_id': good.id, 'quantity': 2})
        order = Order.objects.filter(user_id=user.id).last()
        user.refresh_from_db()
        self.assertEqual(start_balance - good.price * order.quantity, user.profile.balance)

        response = self.client.post(reverse('refuse_url'), {'order': order.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your order was refused!')
        user.refresh_from_db()
        self.assertEqual(start_balance, user.profile.balance)

        response = self.client.post(reverse('refuse_url'), {'order': 100500})
        self.assertEqual(response.status_code, 404)
