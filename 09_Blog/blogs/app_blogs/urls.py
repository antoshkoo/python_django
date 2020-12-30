from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list_url'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail_url'),
    path('create/', PostCreateView.as_view(), name='post_create_url')
]