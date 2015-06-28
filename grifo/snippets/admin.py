from django.contrib import admin
from grifo.snippets.models import Snippet, SnippetCategory


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


class SnippetCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Snippet, SnippetAdmin)
admin.site.register(SnippetCategory, SnippetCategoryAdmin)
