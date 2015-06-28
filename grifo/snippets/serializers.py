from rest_framework import serializers

from grifo.snippets.models import Snippet, SnippetCategory


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('owner', 'category', 'title', 'content', 'url')
        read_only_fields = ('id', 'created_at',)


class SnippetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetCategory
        fields = ('id', 'name',)
        read_only_fields = ('id',)
