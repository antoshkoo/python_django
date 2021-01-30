from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# balance - 10.0
USER_DATA = {
    'username': 'test',
    'password': 'test',
}

# balance - 460.0
USER_DATA_BOSS = {
    'username': 'test2',
    'password': 'test',
}


class UserRegisterViewTest(TestCase):
    def test_user_register_page(self):
        response = self.client.get(reverse('user_register_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertContains(response, '<h1>Register</h1>')
        self.assertContains(response, 'Sign up</button>')
        self.assertContains(response, '<select name="language">')
        self.assertContains(response, '<button type="submit">Select</button>')


class UserLoginViewTest(TestCase):
    def test_user_login_page(self):
        response = self.client.get(reverse('user_login_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertContains(response, '<h1>Sign in</h1>')
        self.assertContains(response, 'Sign in</button>')
        self.assertContains(response, '<select name="language">')
        self.assertContains(response, '<button type="submit">Select</button>')

    def test_user_logged_login_page(self):
        User.objects.create_user(username=USER_DATA['username'], password=USER_DATA['password'])
        self.client.login(username=USER_DATA['username'], password=USER_DATA['password'])
        response = self.client.get(reverse('user_login_url'))
        self.assertRedirects(response, reverse('user_profile_url'), 302, target_status_code=200)


class UserLogoutViewTest(TestCase):
    def test_user_logout_page(self):
        User.objects.create_user(username=USER_DATA['username'], password=USER_DATA['password'])
        self.client.login(username=USER_DATA['username'], password=USER_DATA['password'])
        response = self.client.get(reverse('user_logout_url'))
        self.assertRedirects(response, reverse('main_page_url'), 302, target_status_code=200)


class UserProfileViewTest(TestCase):
    fixtures = ['initial_data.json']

    def test_user_profile_page(self):
        response = self.client.get(reverse('user_profile_url'))
        next_url = reverse('user_login_url') + '?next=' + reverse('user_profile_url')
        self.assertRedirects(response, next_url, 302, target_status_code=200)

    def test_logged_user_profile_page(self):
        self.client.login(username=USER_DATA_BOSS['username'], password=USER_DATA_BOSS['password'])
        self.client.post(reverse('buy_url'), {'good_id': 1, 'quantity': 1})
        user = User.objects.get(username=USER_DATA_BOSS['username'])

        response = self.client.get(reverse('user_profile_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
        self.assertContains(response, 'Shopping history')
        self.assertContains(response, f'<p>Balance: {user.profile.balance}$</p>')
