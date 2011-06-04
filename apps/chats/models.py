from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape, urlize
from django.utils.text import truncate_words

from automatic_timestamps.models import TimestampModel


class Chat(TimestampModel):
    """
    A chat is a single or multi-line text excerpt from a chat (usually
    purposefully out of context) posted by a user. It is often
    view-restricted to specific groups.
    """

    # A chat without any associated Friend Groups is considered public and
    # will be viewable to the entire world!
    friend_groups = models.ManyToManyField('profiles.FriendGroup', blank=True)
    posted_by = models.ForeignKey(User)
    text = models.TextField()

    def as_html(self, tag='div'):
        """
        Return an HTML representation of this chat, including tags marking
        the author and text selection accordingly.
        
        Use the tag argument to customize the tag that wraps each line in
        a chat.
        """

        html = u''
        for line in self.text.splitlines():
            line_sections = escape(line).split(': ', 1)
            if len(line_sections) > 1:
                html += u'<{tag} class="line"><span class="author">{author}: </span><span class="text">{text}</span><span class="post-text"></span></{tag}>'.format(
                    author=line_sections[0],
                    tag=tag,
                    text=urlize(line_sections[1]),
                )
            else:
                html += u'<{tag} class="no-author line"><span class="text">{text}</span><span class="post-text"></span></{tag}>'.format(
                    tag=tag,
                    text=urlize(line_sections[0]),
                )

        return html

    def friend_groups_ordered(self):
        """
        Return all Friend Groups this Chat belongs to, ordered by
        name (ascending).
        """
        return self.friend_groups.all().order_by('name')

    def __unicode__(self):
        """Return the first six words from this chat's text field."""
        return truncate_words(self.text, 6)
