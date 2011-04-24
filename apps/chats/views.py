from django.http import HttpResponse
from django.forms.models import modelformset_factory
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.utils.datastructures import DotExpandedDict
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from chats.models import Chat, Quote

@cache_page(60 * 1)
def index(request):
    """Display the site's root/home page."""
    
    return render_to_response('index.html', {
        
    }, context_instance=RequestContext(request))

def show(request, id):
    """
    Show a single Quote, including its author. If this quote belongs
    to any Friend Groups, make sure the current user is in at least
    one of the groups.
    """
    
    quote = get_object_or_404(Quote, id=id)
    
    # Authenticated user (or no authentication is required)
    if bool(quote.friend_groups.exists()) == False or (request.user.is_authenticated() and request.user.get_profile().in_friend_groups(quote.friend_groups)):
        return render_to_response('show.html', {
            'quote': quote
        }, context_instance=RequestContext(request))
    else: # Current user isn't allowed to see this quote
        return render(request, 'show.html', {
            
        }, context_instance=RequestContext(request), status=403)
