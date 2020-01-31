from django.db import models
from uuid import uuid4

class AppDataBase(models.Model):

    uuid  = models.CharField(primary_key = True, max_length = 50)
    title = models.CharField(max_length = 50)
    state = models.CharField(max_length = 10, null = True)
    owner = models.CharField(max_length = 10, null = True)

    def __unicode__(self):
        return self.uuid
