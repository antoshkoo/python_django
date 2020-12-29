from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from .views import ItemListView, upload_price, upload_file

urlpatterns = [
    path('', ItemListView.as_view(), name='goods_list_url'),
    path('upload_price/', upload_price, name='upload_price_url'),
    path('upload_file/', upload_file, name='upload_file_url'),
]
