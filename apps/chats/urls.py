from django.conf.urls.defaults import *
from chats.views import *

urlpatterns = patterns('',
    url('^$', index, name='chats_index'),
    url('^quotes/new$', new, name='chats_new'),
    url('^quotes/(?P<id>\d+)$', show, name='chats_show'),
)
