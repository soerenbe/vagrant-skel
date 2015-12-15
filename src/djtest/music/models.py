from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return self.name
