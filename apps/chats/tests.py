from django.test import TestCase
from django.test.client import Client

from django.contrib.auth.models import User
from chats.models import *
from profiles.models import *


DEFAULT_PASSWORD = 'foobarpass'
LOREM = 'Lorem ipsum dolor sit amet.'

class QuoteTest(TestCase):
    def test_quote_optional_relationships(self):
        """
        Tests that a quote can exist with or without a related Chat object.
        """
        
        user = User.objects.create_user('duffman', 'duffman@test.com', DEFAULT_PASSWORD)
        user.save()
        
        chat = Chat(title='We discussed things over many lines')
        chat.save()
        
        quote_with_chat = Quote(text=LOREM, posted_by=user, chat=chat)
        quote_with_chat.save()
        
        quote_without_chat = Quote(text=LOREM, posted_by=user)
        quote_without_chat.save()
        
        self.assertTrue(quote_with_chat.id)
        self.assertIsNotNone(quote_with_chat.chat)
        self.assertTrue(quote_without_chat.id)
        self.assertIsNone(quote_without_chat.chat)
    
    def test_friendgroup_authorizations(self):
        """
        Test that chats and quotes are protected accordingly for different users.
        """
        
        friendgroup_no_matts_allowed = FriendGroup(name='No Matts Allowed!')
        friendgroup_no_matts_allowed.save()
        # "webchat" was the name of our usual Jabber room in iChat at NS Government :-)
        friendgroup_webchat = FriendGroup(name='webchat')
        friendgroup_webchat.save()
        
        user_matt = User.objects.create_user('matt', 'test@test.com', DEFAULT_PASSWORD)
        user_matt.save()
        user_matt.get_profile().friend_groups.add(friendgroup_webchat)
        
        quote_anon = Quote(text=LOREM, posted_by=user_matt)
        quote_anon.save()
        
        quote_no_matts = Quote(text=LOREM, posted_by=user_matt)
        quote_no_matts.save()
        quote_no_matts.friend_groups.add(friendgroup_no_matts_allowed)
        
        quote_webchat = Quote(text=LOREM, posted_by=user_matt)
        quote_webchat.save()
        quote_webchat.friend_groups.add(friendgroup_webchat)
        
        client_matt = Client()
        client_matt.login(username='matt', password=DEFAULT_PASSWORD)
        # Test logged-in user accessing anonymous and protected quotes
        response = client_matt.get('/quotes/{id}'.format(id=quote_anon.id))
        self.assertEquals(response.status_code, 200)
        response = client_matt.get('/quotes/{id}'.format(id=quote_no_matts.id))
        self.assertEquals(response.status_code, 403)
        response = client_matt.get('/quotes/{id}'.format(id=quote_webchat.id))
        self.assertEquals(response.status_code, 200)
        
        client_anon = Client()
        # Test anonymous user accessing anonymous quotes
        response = client_anon.get('/quotes/{id}'.format(id=quote_anon.id))
        self.assertEquals(response.status_code, 200)
        # Test anonymous user accessing protected quotes
        response = client_anon.get('/quotes/{id}'.format(id=quote_webchat.id))
        self.assertEquals(response.status_code, 403)
