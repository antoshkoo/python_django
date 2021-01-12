from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


USER_EMAIL = 'test@company.com'
OLD_PASSWORD = 'testpassword'


class TestRestorePassword(TestCase):

    def test_restore_password(self):
        response = self.client.get(reverse('restore_password_url'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('restore_password_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='restore_password.html')

    def test_correct_context(self):
        response = self.client.get(reverse('restore_password_url'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Reset')

    def test_post_restore_password(self):
        user = User.objects.create(username='Test', email=USER_EMAIL)
        response = self.client.post(reverse('restore_password_url'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 200)
        from django.core.mail import outbox
        self.assertEqual(len(outbox), 1)
        self.assertIn(USER_EMAIL, outbox[0].to)

    def test_if_password_change(self):
        user = User.objects.create(username='Test', email=USER_EMAIL)
        user.set_password(OLD_PASSWORD)
        user.save()
        old_password_hash = user.password
        response = self.client.post(reverse('restore_password_url'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 200)
        user.refresh_from_db()
        self.assertNotEqual(old_password_hash, user.password)
