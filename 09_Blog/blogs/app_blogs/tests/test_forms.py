from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.utils.six import BytesIO

from app_blogs.forms import PostForm, PostFileUpload
from app_blogs.models import Post


class PostFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test', password='test')

    def test_post_form_valid(self):
        form_data = {'title': '1 Post', 'body': '1 post body'}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_form_title_label(self):
        form = PostForm()
        self.assertEqual(form.fields['title'].label, 'Заголовок')

    def test_post_form_body_label(self):
        form = PostForm()
        self.assertEqual(form.fields['body'].label, 'Описание')

    def test_post_form_image_label(self):
        form = PostForm()
        self.assertEqual(form.fields['files'].label, 'Картинки')

    def test_post_form_data_no_image_submit(self):
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('post_create_url'), {'title': 'First post', 'body': 'Post body'})
        self.assertRedirects(response, reverse('posts_list_url'), status_code=302, target_status_code=200)

    def test_post_form_data_with_image_submit(self):
        self.client.login(username='test', password='test')

        img = BytesIO(
            b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00'
            b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')
        image_file = SimpleUploadedFile('image.gif', img.read(), 'image/gif')

        response = self.client.post(reverse('post_create_url'), {
            'title': 'First post',
            'body': 'Post body',
            'files': image_file})
        self.assertRedirects(response, reverse('posts_list_url'), status_code=302, target_status_code=200)

        post = Post.objects.first()
        self.assertEqual(post.title, 'First post')
        self.assertTrue(post.gallery.first().image)

        post.gallery.first().delete()


class PostFileUploadTest(TestCase):

    def test_post_file_upload_file_label(self):
        form = PostFileUpload()
        self.assertEqual(form.fields['file'].label, 'Файл *.csv')

    def test_post_file_upload_file_submit(self):
        user = User.objects.create_user(username='admin', password='admin')
        user.is_staff = True
        user.save()
        self.client.login(username='admin', password='admin')

        file = SimpleUploadedFile('text.csv', b'Post Title,Post Body,2020-12-12,4')
        response = self.client.post(reverse('post_upload_url'), {'file': file})
        self.assertEqual(response.status_code, 200)

        post = Post.objects.first()
        self.assertEqual(post.title, 'Post Title')
