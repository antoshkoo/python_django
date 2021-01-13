from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_users.forms import UserRegisterForm, UserEditForm, ProfileEditForm

USER_REGISTER_FORM_DATA = {
    'username': 'test',
    'email': 'test@test.com',
    'password1': 'password',
    'password2': 'password'
}


class UserRegisterFormTest(TestCase):
    def test_user_register_form_valid(self):
        form = UserRegisterForm(data=USER_REGISTER_FORM_DATA)
        self.assertTrue(form.is_valid())

    def test_user_register_form_labels(self):
        form = UserRegisterForm()
        self.assertEqual(form.fields['username'].label, 'Имя пользователя')
        self.assertEqual(form.fields['email'].label, 'Адрес электронной почты')
        self.assertEqual(form.fields['password1'].label, 'Пароль')
        self.assertEqual(form.fields['password2'].label, 'Подтверждение пароля')

    def test_user_register_form_post(self):
        response = self.client.post(reverse('user_register_url'), USER_REGISTER_FORM_DATA)
        user = User.objects.first()
        self.assertEqual(user.username, USER_REGISTER_FORM_DATA['username'])
        self.assertRedirects(response, reverse('posts_list_url'), status_code=302, target_status_code=200)


class UserEditFormTest(TestCase):

    def test_user_edit_form_valid(self):
        form = UserEditForm(data={'first_name': 'test first', 'last_name': 'test last'})
        self.assertTrue(form.is_valid())

    def test_user_edit_form_labels(self):
        form = UserEditForm()
        self.assertEqual(form.fields['first_name'].label, 'Имя')
        self.assertEqual(form.fields['last_name'].label, 'Фамилия')

    def test_user_edit_form_post(self):
        User.objects.create_user(username='user', password='pass')
        self.client.login(username='user', password='pass')
        response = self.client.post(reverse('user_profile_url'), {'first_name': 'test 1', 'last_name': 'test 2'})
        self.assertRedirects(response, reverse('user_profile_url'), status_code=302, target_status_code=200)

        user = User.objects.first()
        self.assertEqual(user.first_name, 'test 1')


class ProfileEditFormTest(TestCase):
    def test_profile_edit_form_valid(self):
        form = ProfileEditForm(data={'first_name': 'test first', 'last_name': 'test last'})
        self.assertTrue(form.is_valid())

    def test_profile_edit_form_labels(self):
        form = ProfileEditForm()
        self.assertEqual(form.fields['about'].label, 'О себе')
        self.assertEqual(form.fields['avatar'].label, 'Аватар')

    def test_profile_edit_form_post(self):
        User.objects.create_user(username='user', password='pass')
        self.client.login(username='user', password='pass')
        response = self.client.post(reverse('user_profile_url'), {'about': 'test about', 'avatar': 'test 2'})
        self.assertRedirects(response, reverse('user_profile_url'), status_code=302, target_status_code=200)

        user = User.objects.first()
        self.assertEqual(user.profile.about, 'test about')
