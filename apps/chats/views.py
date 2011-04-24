from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from chats.forms import *
from chats.models import *


@cache_page(60 * 1)
def index(request):
    """Display the site's root/home page."""
    
    return render_to_response('index.html', {
        
    }, context_instance=RequestContext(request))

def show(request, id):
    """
    Show a single Chat, with formatting to show each line's author.
    If this quote belongs to any Friend Groups, make sure the current
    user is in at least one of the groups.
    """
    
    chat = get_object_or_404(Chat, id=id)
    
    # Authenticated user (or no authentication is required)
    if bool(chat.friend_groups.exists()) == False or (request.user.is_authenticated() and request.user.get_profile().in_friend_groups(chat.friend_groups)):
        return render_to_response('show.html', {
            'chat': chat,
        }, context_instance=RequestContext(request))
    else: # Current user isn't allowed to see this quote
        return render(request, 'show.html', {
            
        }, context_instance=RequestContext(request), status=403)

def new(request):
    """Display the form to add a new quote to the database."""
    
    form = PublicChatForm()
    
    return render_to_response('new.html', {
        'chat': chat,
        'form': form,
    }, context_instance=RequestContext(request))
