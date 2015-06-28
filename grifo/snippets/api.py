from grifo.snippets.models import Snippet, SnippetCategory
from rest_framework import viewsets

from grifo.snippets.serializers import SnippetSerializer, SnippetCategorySerializer


class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    lookup_field = 'id'


class SnippetCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetCategorySerializer
    queryset = SnippetCategory.objects.all()
    lookup_field = 'id'
