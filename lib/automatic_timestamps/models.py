from django.db import models

import datetime


class TimestampModel(models.Model):
    """
    Extend the default Django model to add timestamps to all objects.
    """
    
    class Meta:
        abstract = True
    
    # Timestamps!
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        """
        Override the save method to automatically set the created_at and
        updated_at fields with current date info.
        """
        if self.created_at == None:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
        super(TimestampModel, self).save()
