from django.test import TestCase

from django.db import models
from automatic_timestamps.models import TimestampModel

from time import sleep


class GenericTimestampTestModel(TimestampModel):
    """A generic, boring model to test timestamp creation against."""
    pass

class TimestampModelTest(TestCase):
    def test_timestamps_are_saved_automatically(self):
        """Test that timestamps are set when a model is saved."""
        model = GenericTimestampTestModel()
        model.save()
        
        self.assertTrue(model.created_at)
        self.assertTrue(model.updated_at)
    
    def test_timestamp_is_updated(self):
        """Test that the updated_at field is set on save()."""
        model = GenericTimestampTestModel()
        model.save()
        
        last_time_saved = model.updated_at
        
        sleep(1)
        
        model.save()
        
        self.assertNotEqual(last_time_saved, model.updated_at)
    
    def test_created_timestamp_is_not_updated(self):
        """Test that the created_at field is not changed on subsequent saves."""
        model = GenericTimestampTestModel()
        model.save()
        
        created = model.created_at
        
        sleep(1)
        
        model.save()
        
        self.assertEqual(created, model.created_at)
        