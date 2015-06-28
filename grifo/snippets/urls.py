from django.conf.urls import include, url

from grifo.snippets import views

urlpatterns = [
    url(r'^$', views.snippets_index, name='snippets.index'),
]
