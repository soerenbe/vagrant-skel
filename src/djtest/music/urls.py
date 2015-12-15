# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import IndexView, ArtistListView, AlbumListView, TitleListView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^artist/$', ArtistListView.as_view(), name='artist-list'),
    url(r'^album/$', AlbumListView.as_view(), name='album-list'),
    url(r'^title/$', TitleListView.as_view(), name='title-list'),
]