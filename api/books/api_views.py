from books.models import Author
from books.serializers import AuthorSerializer
from rest_framework import viewsets

class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Author.objects.filter(deleted_at=None)
    serializer_class = AuthorSerializer

