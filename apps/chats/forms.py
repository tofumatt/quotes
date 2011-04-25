from django import forms
from django.contrib.auth.models import User

from chats.models import Chat
from profiles.models import FriendGroup


class PublicChatForm(forms.ModelForm):
    """Public-facing Chat form used in the web-interface for users."""
    
    class Meta:
        fields = (
            'friend_groups',
            'text',
        )
        model = Chat
