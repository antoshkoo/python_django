from django.db.models import Sum
from rest_framework import serializers

from app_catalog.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField('get_total')

    class Meta:
        queryset = Author.objects.all()
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'total']

    def get_total(self, obj):
        query = Book.objects.filter(author=obj)
        total = query.aggregate(Sum('pages'))
        total['books__sum'] = len(query)
        return total


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'published', 'pages', 'author']
