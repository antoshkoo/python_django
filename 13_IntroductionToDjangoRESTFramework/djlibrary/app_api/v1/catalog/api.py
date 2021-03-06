from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from app_api.v1.catalog.permissions import ReadOnly
from app_api.v1.catalog.serializers import AuthorSerializer, BookSerializer
from app_catalog.models import Author, Book


class LimitPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('pk')
    serializer_class = AuthorSerializer
    pagination_class = LimitPagination
    permission_classes = [IsAdminUser | ReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('pk')
    serializer_class = BookSerializer
    pagination_class = LimitPagination
    permission_classes = [IsAdminUser | ReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    @action(detail=True, methods=['post'])
    def set_active(self, request, pk=None):
        book = self.get_object()
        book.set_active()
        book.save()
        return Response({'status': f'Active status was changed'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Book.objects.filter(is_active=True).order_by('pk')
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

