from rest_framework import serializers

from grifo.snippets.models import Snippet, SnippetCategory


class SnippetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetCategory
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class SnippetSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name

    class Meta:
        model = Snippet
        fields = ('id', 'owner', 'category', 'category_name', 'title', 'content', 'description', 'url', 'updated_at')
        read_only_fields = ('id', 'created_at', 'category_name')