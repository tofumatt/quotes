from django.test import TestCase
from django.test.client import Client

from django.contrib.auth.models import User
from chats.models import *
from profiles.models import *


DEFAULT_AUTHOR = 'Ned Flanders'
DEFAULT_PASSWORD = 'foobarpass'
LOREM = 'Lorem ipsum dolor sit amet.'

class ChatTest(TestCase):
    def test_friendgroup_authorizations(self):
        """Test that chats are protected accordingly for different users."""

        friendgroup_no_matts_allowed = FriendGroup(name='No Matts Allowed!')
        friendgroup_no_matts_allowed.save()
        # "webchat" was the name of our usual Jabber room in iChat at NS Government :-)
        friendgroup_webchat = FriendGroup(name='webchat')
        friendgroup_webchat.save()

        user_matt = User.objects.create_user(
            'matt', 'test@test.com', DEFAULT_PASSWORD)
        user_matt.save()
        user_matt.get_profile().friend_groups.add(friendgroup_webchat)

        chat_anon = Chat(text=LOREM, posted_by=user_matt)
        chat_anon.save()

        chat_no_matts = Chat(text=LOREM, posted_by=user_matt)
        chat_no_matts.save()
        chat_no_matts.friend_groups.add(friendgroup_no_matts_allowed)

        chat_webchat = Chat(text=LOREM, posted_by=user_matt)
        chat_webchat.save()
        chat_webchat.friend_groups.add(friendgroup_webchat)

        client_matt = Client()
        client_matt.login(username='matt', password=DEFAULT_PASSWORD)
        # Test logged-in user accessing anonymous and protected quotes
        response = client_matt.get('/chats/{id}'.format(id=chat_anon.id))
        self.assertEquals(response.status_code, 200)
        response = client_matt.get('/chats/{id}'.format(id=chat_no_matts.id))
        self.assertEquals(response.status_code, 403)
        response = client_matt.get('/chats/{id}'.format(id=chat_webchat.id))
        self.assertEquals(response.status_code, 200)

        client_anon = Client()
        # Test anonymous user accessing anonymous quotes
        response = client_anon.get('/chats/{id}'.format(id=chat_anon.id))
        self.assertEquals(response.status_code, 200)
        # Test anonymous user accessing protected quotes
        response = client_anon.get('/chats/{id}'.format(id=chat_webchat.id))
        self.assertEquals(response.status_code, 403)
