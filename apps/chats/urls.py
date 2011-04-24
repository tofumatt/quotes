from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('^$', 'chats.views.index', name='chats_index'),
    url('^chats/new$', 'chats.views.new', name='chats_new'),
    url('^chats/(?P<id>\d+)$', 'chats.views.show', name='chats_show'),
)
