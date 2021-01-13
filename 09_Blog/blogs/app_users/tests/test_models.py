from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils.six import BytesIO

from app_blogs.models import Post


class ProfileModelTest(TestCase):
    def test_profile_model(self):
        user = User.objects.create_user(username='test', password='test')

        img = BytesIO(
            b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00'
            b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')
        image_file = SimpleUploadedFile('image.gif', img.read(), 'image/gif')

        user.profile.about = 'test about'
        user.profile.avatar = image_file
        user.save()

        self.assertTrue(user.profile.avatar)
        self.assertEqual(user.profile.about, 'test about')

        user.profile.avatar.delete()
