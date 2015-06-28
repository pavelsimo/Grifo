import logging

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

logger = logging.getLogger(__name__)


class SnippetCategory(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Snippet Category')
        db_table = 'snippet_category'


class Snippet(models.Model):
    # Foreign keys
    owner = models.ForeignKey(User, null=True)
    category = models.ForeignKey(SnippetCategory)

    # Fields
    title = models.CharField(max_length=255, blank=False, verbose_name=_('Title'))
    content = models.TextField(max_length=10000, blank=False, verbose_name=_('Content'))
    description = models.TextField(max_length=10000, blank=True, verbose_name=_('Description'))
    url = models.CharField(max_length=255, blank=True, verbose_name=_('Url'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Snippet')
        db_table = 'snippet'
