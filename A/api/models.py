from django.db import models
from uuid import uuid4

# Create your models here.

class VacanciesDataBase(models.Model):

    uuid  = models.CharField(primary_key = True, default = uuid4, max_length = 50)
    title = models.CharField(max_length = 50)
    description = models.TextField(null = True)
    state = models.CharField(max_length = 10, null = True)
    owner = models.CharField(max_length = 10,null = True)

    def __unicode__(self):
        return self.uuid
