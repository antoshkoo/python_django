from rest_framework import viewsets, filters
from rest_framework.permissions import IsAdminUser

from app_api.v1.catalog.permissions import ReadOnly
from app_api.v1.catalog.serializers import AuthorSerializer, BookSerializer
from app_catalog.models import Author, Book


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        queryset = Book.objects.all()
        filter_author = self.request.query_params.get('author')
        filter_pages = self.request.query_params.get('pages')
        filter_pages_params = self.request.query_params.get('filter')
        if filter_author:
            queryset = queryset.filter(author=filter_author)
        if filter_pages:
            if filter_pages_params == 'more':
                queryset = queryset.filter(pages__gt=filter_pages)
            elif filter_pages_params == 'less':
                queryset = queryset.filter(pages__lt=filter_pages)
            else:
                queryset = queryset.filter(pages=filter_pages)
        return queryset

