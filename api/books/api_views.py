
from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.utils import timezone

class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Author.objects.filter(deleted_at=None)
    serializer_class = AuthorSerializer

    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        include = request.GET.get('include', '')
        if include != '':
            include = include.split(',')
            if 'books' in include:
                instance.books = Book.objects.filter(author=instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    """
    Soft delete a model instance.
    """
    def destroy(self, request, pk=None):
        author = self.get_object()
        author.deleted_at = timezone.now()
        author.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Book.objects.filter(deleted_at=None)
    serializer_class = BookSerializer
