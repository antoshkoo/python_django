from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_blogs.models import Post

NUMBER_OF_POSTS = 10


class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test', password='password')
        for new_post in range(NUMBER_OF_POSTS):
            Post.objects.create(title=f'Post {new_post}', body=f'Post content {new_post}', user_id=user.id)

    def test_post_list_status(self):
        response = self.client.get(reverse('posts_list_url'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_template(self):
        response = self.client.get(reverse('posts_list_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blogs/post_list.html')

    def test_post_list_header(self):
        response = self.client.get(reverse('posts_list_url'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Записи</h1>')

    def test_post_list_len(self):
        response = self.client.get(reverse('posts_list_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['post_list']) == 10)


class PostDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test', password='password')
        Post.objects.create(title=f'Post', body=f'Post content', user_id=user.id)

    def test_post_detail_status(self):
        response = self.client.get(reverse('post_detail_url', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_template(self):
        response = self.client.get(reverse('post_detail_url', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blogs/post_detail.html')

    def test_post_detail_header(self):
        response = self.client.get(reverse('post_detail_url', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post')

    def test_post_detail_author(self):
        response = self.client.get(reverse('post_detail_url', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<strong>test</strong>')

    def test_post_detail_body(self):
        response = self.client.get(reverse('post_detail_url', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post content')


class PostCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test', password='password')

    def test_post_create_not_logged_user_redirect(self):
        response = self.client.get(reverse('post_create_url'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/posts/create/')

    def test_post_create_logged_user_status(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('post_create_url'))
        self.assertEqual(response.status_code, 200)

    def test_post_create_template(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('post_create_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blogs/post_form.html')

    def test_post_create_header(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('post_create_url'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Создание записи</h1>')

    def test_post_create_form(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('post_create_url'))
        self.assertTrue('form' in response.context)


class PostUploadViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_simple = User.objects.create_user(username='test', password='test')
        user_staff = User.objects.create_user(username='admin', password='admin')
        user_staff.is_staff = True
        user_staff.save()

    def test_post_upload_user_not_logged_redirect(self):
        response = self.client.get(reverse('post_upload_url'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/posts/upload/')

    def test_post_upload_user_simple_logged_redirect(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('post_upload_url'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Недостаточно прав')

    def test_post_upload_user_staff_logged(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('post_upload_url'))
        self.assertEqual(response.status_code, 200)

    def test_post_upload_user_staff_template(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('post_upload_url'))
        self.assertTemplateUsed(response, 'app_blogs/post_upload.html')

    def test_post_upload_user_staff_header(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('post_upload_url'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Загрузка записей</h1>')

    def test_post_upload_user_staff_form(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('post_upload_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
