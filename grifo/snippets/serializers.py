from rest_framework import serializers

from grifo.snippets.models import Snippet, SnippetCategory


class SnippetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetCategory
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class SnippetSerializer(serializers.ModelSerializer):
    category = SnippetCategorySerializer(read_only=True, many=False)

    class Meta:
        model = Snippet
        fields = ('id', 'owner', 'category', 'title', 'content', 'url')
        read_only_fields = ('id', 'created_at',)