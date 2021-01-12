from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from app_blogs.models import Post, Gallery


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test', password='test')
        Post.objects.create(title='1 Post', body='1 post body', user_id=user.id)

    def test_post_model_title_label(self):
        post = Post.objects.first()
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок')

    def test_post_model_body_label(self):
        post = Post.objects.first()
        field_label = post._meta.get_field('body').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_post_model_title_max_length(self):
        post = Post.objects.first()
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)


class GalleryModelTest(TestCase):

    def test_gallery_model_file_field(self):
        user = User.objects.create_user(username='test', password='test')
        post = Post.objects.create(title='1 Post', body='1 post body', user_id=user.id)

        image_url = 'https://yastatic.net/islands/_/RQWGFypkIRAzEbaERs_Sq8zKRzY.svg'
        image_data = self.client.get(image_url).content
        image_file = SimpleUploadedFile('image.jpg', image_data, 'image/jpeg')
        gallery = Gallery.objects.create(image=image_file, post_id=post.id)

        self.assertTrue(gallery.image)
