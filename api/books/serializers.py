from rest_framework import serializers
from books.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

    def create(self, validated_data):
        """
        Create and return a new `Show` instance, given the validated data.
        """
        return Author.objects.create(**validated_data)