from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateFormView, NewsEditFormView, NewsCommentsFormView

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/news_create.html', NewsCreateFormView.as_view(), name='news_create'),
    path('news/<int:news_id>/edit/', NewsEditFormView.as_view(), name='news_edit'),
    path('news/<int:news_id>/comment/', NewsCommentsFormView.as_view(), name='news_comment'),
]