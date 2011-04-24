from django.test import TestCase
from django.test.client import Client

from django.contrib.auth.models import User
from chats.models import *
from profiles.models import *


class ProfileTest(TestCase):
    def test_profile_is_created_automatically(self):
        """
        Tests that a UserProfile is created automatically whenever a User
        is created.
        """
        
        user = User.objects.create_user('duffman', 'duffman@test.com', 'pass')
        user.save()
        self.assertTrue(user.get_profile())
