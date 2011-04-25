from django.conf.urls.defaults import *

urlpatterns = patterns('chats.views',
    url('^chats/$', 'index', name='chats_index'),
    url('^chats/new/$', 'new', name='chats_new'),
    url('^chats/(?P<id>\d+)/$', 'show', name='chats_show'),
)
