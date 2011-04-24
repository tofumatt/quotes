from django.db import models
from annoying.decorators import signals
from annoying.fields import AutoOneToOneField
from automatic_timestamps.models import TimestampModel

from django.contrib.auth.models import User


class FriendGroup(TimestampModel):
    """
    A group of users who identify as each other's friends and can
    create/view chats and quotes in this group.
    """
    
    admins = models.ManyToManyField(User)
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        """Return the name of this FriendGroup."""
        return self.name

class UserProfile(TimestampModel):
    """
    User profile extensions to provide extra attributes and relations
    to a User object.
    """
    
    friend_groups = models.ManyToManyField(FriendGroup, blank=True)
    user = AutoOneToOneField(User)
    
    def in_friend_groups(self, groups):
        """
        Check to see if this User is part of any of the supplied friend_groups.
        If the user is a member of any of the groups (or no friend_groups exist),
        we return True.
        """
        
        return bool(
            bool(groups.exists()) == False
            or
            self.friend_groups.filter(id__in=groups.all().values_list('id')).exists()
        )
    
    def __unicode__(self):
        """Return the username this profile belongs to."""
        return self.user.username

@signals.post_save(sender=User)
def create_user_profile_for_user(instance, created, **kwargs):
    """
    Automatically create an associated UserProfile for every created User.
    
    Using a post_save hook (only when a User is created), then accessing our
    AutoOneToOneField creates a profile. Wheee.
    """
    
    if not created:
        return
    
    instance.userprofile # AutoOneToOneField creates the object when accessed
