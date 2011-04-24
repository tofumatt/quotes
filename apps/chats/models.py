from django.db import models
from django.contrib.auth.models import User
from django.utils.text import truncate_words

from automatic_timestamps.models import TimestampModel


class Chat(TimestampModel):
    """
    A collection of chat items (quotes), ordered by their created_at values,
    grouped together like a chat history. All quotes that belong to a Chat are
    not displayable on an individual basis.
    """
    
    title = models.CharField(max_length=200)

class Quote(TimestampModel):
    """
    A quote is a single-line text excerpt from a chat (usually purposefully
    out of context) belonging to a certain user. It is often view-restricted to
    specific groups.
    """
    
    # Chat relationships are nullable; most Quotes likely don't have a related
    # Chat object.
    chat = models.ForeignKey(Chat, blank=True, null=True)
    # A quote without any associated Friend Groups is considered public and will
    # be viewable to the entire world!
    friend_groups = models.ManyToManyField('profiles.FriendGroup', blank=True)
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        """
        Return the text found inside this quote.
        """
        return u"{name}: {text_excerpt}".format(
            name=self.user.username,
            text_excerpt=self.text# truncate_words(self.text, 5)
        )
