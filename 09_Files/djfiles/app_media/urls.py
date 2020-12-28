from django.urls import path
from .views import upload_file, upload_file_check

urlpatterns = [
    path('upload_file/', upload_file, name='upload_file_url'),
    path('upload_file_check/', upload_file_check, name='upload_file_check_url')
]