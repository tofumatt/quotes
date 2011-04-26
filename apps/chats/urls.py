from django.conf.urls.defaults import *

urlpatterns = patterns('chats.views',
    url('^chats/$', 'index', name='chats-index'),
    url('^chats/new/$', 'new', name='chats-new'),
    url('^chats/(?P<id>\d+)/$', 'show', name='chats-show'),
)
