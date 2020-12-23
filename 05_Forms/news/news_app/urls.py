from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('create/', NewsCreateFormView.as_view(), name='news_create'),
    path('<int:news_id>/edit/', NewsEditFormView.as_view(), name='news_edit'),
    path('<int:news_id>/comment/', NewsCommentsFormView.as_view(), name='news_comment'),
]