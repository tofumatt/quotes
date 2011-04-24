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
    out of context) posted by a user. It is often view-restricted to
    specific groups.
    """
    
    author = models.CharField(max_length=80)
    # Most Quotes likely don't have a related Chat object.
    chat = models.ForeignKey(Chat, blank=True, null=True)
    # A quote without any associated Friend Groups is considered public and will
    # be viewable to the entire world!
    friend_groups = models.ManyToManyField('profiles.FriendGroup', blank=True)
    posted_by = models.ForeignKey(User)
    text = models.CharField(max_length=1000)
    
    def __unicode__(self):
        """
        Return the name of the quote's authoor and text found inside
        this quote.
        """
        return u"{author}: {text_excerpt}".format(
            author=self.author,
            text_excerpt=self.text# truncate_words(self.text, 5)
        )
