from django.db import models
from django.contrib.auth.models import User
from django.utils.text import truncate_words

from automatic_timestamps.models import TimestampModel


class Chat(TimestampModel):
    """
    A chat is a single or multi-line text excerpt from a chat (usually
    purposefully out of context) posted by a user. It is often
    view-restricted to specific groups.
    """
    
    # A chat without any associated Friend Groups is considered public and will
    # be viewable to the entire world!
    friend_groups = models.ManyToManyField('profiles.FriendGroup', blank=True)
    posted_by = models.ForeignKey(User)
    text = models.TextField()
    
    def __unicode__(self):
        """Return the first six words from this chat's text field."""
        return truncate_words(self.text, 6)
