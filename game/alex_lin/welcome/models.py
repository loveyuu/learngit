# encoding=utf-8
from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __unicode__(self):
        return self.title


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``create`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Flavor(TimeStampedModel):
    title = models.CharField(max_length=200)



