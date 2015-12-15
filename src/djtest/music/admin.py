# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.contrib import admin
from .models import Album, Artist, Title


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name']


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'album']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Title, TitleAdmin)
