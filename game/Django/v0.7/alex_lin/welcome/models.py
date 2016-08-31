from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __unicode__(self):
        return self.title

