from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.utils.six import BytesIO

from app_users.models import Profile


class UserRegisterViewTest(TestCase):

    def test_user_register_page(self):
        response = self.client.get(reverse('user_register_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertContains(response, '<h1>Регистрация пользователя</h1>')
        self.assertContains(response, 'Зарегистрироваться</button>')

    def test_user_register_logged_user(self):
        User.objects.create_user(username='user', password='test')
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('user_register_url'))
        self.assertRedirects(response, reverse('user_profile_url'), 302, target_status_code=200)


class UserDetailViewTest(TestCase):

    def test_user_detail_page(self):
        user = User.objects.create_user(username='test', password='test')
        response = self.client.get(reverse('user_detail_url', kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'<h1>Профиль пользователя {user.username}</h1>')


class UserProfileViewTest(TestCase):

    def test_user_profile_page(self):
        user = User.objects.create_user(username='test', password='test')
        user.email = 'test@test.ru'
        user.first_name = 'Test first'
        user.last_name = 'Test last'
        user.save()

        avatar = BytesIO(
            b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00'
            b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')
        avatar_file = SimpleUploadedFile('image.gif', avatar.read(), 'image/gif')
        Profile.objects.create(about='About me', avatar=avatar_file, user_id=user.id)

        self.client.login(username='test', password='test')
        response = self.client.get(reverse('user_profile_url'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'<h3>Привет, {user.username}!</h3>')
        self.assertContains(response, f'{user.email}')
        self.assertContains(response, f'{user.first_name}')
        self.assertContains(response, f'{user.last_name}')
        self.assertContains(response, f'{user.profile.about}')
        self.assertContains(response, f'{user.profile.avatar}')


class UserLogoutViewTest(TestCase):
    def test_user_logout(self):
        User.objects.create_user(username='user', password='password')
        self.client.login(username='user', password='password')

        response = self.client.get(reverse('user_profile_url'))
        self.assertEqual(response.status_code, 200)

        self.client.get(reverse('logout_url'))
        response = self.client.get(reverse('user_profile_url'))
        self.assertEqual(response.status_code, 302)


class UserLoginViewTest(TestCase):

    def test_user_login_page(self):
        response = self.client.get(reverse('login_url'))
        self.assertContains(response, '<h1>Страница входа</h1>')
        self.assertTrue('form' in response.context)

        User.objects.create_user(username='user', password='password')
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('login_url'))
        self.assertRedirects(response, reverse('user_profile_url'), status_code=302, target_status_code=200)