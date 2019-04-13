
from rest_framework import serializers
from books.models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class AuthorBookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = ('id', 'first_name', 'last_name')
    
    _author = AuthorBookSerializer(source='author', many=False, read_only=True)
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', '_author', 'publisher', 'published_date', 'description', 'language')
        extra_kwargs = {
            'author': {'write_only': True}
        }

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
