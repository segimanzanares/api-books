from rest_framework import serializers
from books.models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publisher', 'published_date', 'description', 'language')

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')

    def create(self, validated_data):
        """
        Create and return a new `Show` instance, given the validated data.
        """
        return Author.objects.create(**validated_data)
