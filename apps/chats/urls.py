from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('^$', 'chats.views.index', name='chats_index'),
    url('^quotes/new$', 'chats.views.new', name='chats_new'),
    url('^quotes/(?P<id>\d+)$', 'chats.views.show', name='chats_show'),
)
