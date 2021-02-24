from django.urls import include, path
from rest_framework import routers

from app_api.v1.catalog.api import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]