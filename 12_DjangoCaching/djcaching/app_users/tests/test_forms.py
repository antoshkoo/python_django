from django.test import TestCase
from django.urls import reverse

from app_users.forms import UserRegisterForm


USER_REGISTER_FORM_DATA = {
    'username': 'testuser',
    'password1': 'password',
    'password2': 'password'
}


class UserRegisterFormTest(TestCase):
    def test_user_register_form_valid(self):
        form = UserRegisterForm(data=USER_REGISTER_FORM_DATA)
        self.assertTrue(form.is_valid())

    def test_user_register_form_labels(self):
        form = UserRegisterForm()
        self.assertEqual(form.fields['username'].label, 'Username')
        self.assertEqual(form.fields['password1'].label, 'Password')
        self.assertEqual(form.fields['password2'].label, 'Password confirmation')

    def test_user_register_form_post(self):
        response = self.client.post(reverse('user_register_url'), USER_REGISTER_FORM_DATA)
        self.assertRedirects(response, reverse('user_profile_url'), status_code=302, target_status_code=200)