# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

import django_tables2 as tables

from .models import Artist, Album, Title


class IndexView(TemplateView):
    template_name = 'index.html'


class CustomTable(tables.Table):
    class Meta:
        attrs = {"class": "table table-striped table-condensed"}


class ArtistTable(CustomTable):
    class Meta(CustomTable.Meta):
        model = Artist


class TitleTable(CustomTable):
    class Meta(CustomTable.Meta):
        model = Title


class AlbumTable(CustomTable):
    class Meta(CustomTable.Meta):
        model = Album


class ArtistListView(TemplateView):
    template_name = 'list.html'
    title = "Some Arists"

    def get_context_data(self, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)
        context['table'] = ArtistTable(Artist.objects.all())
        return context


class TitleListView(TemplateView):
    template_name = 'list.html'
    title = "Some Titles"

    def get_context_data(self, **kwargs):
        context = super(TitleListView, self).get_context_data(**kwargs)
        context['table'] = TitleTable(Title.objects.all())
        return context


class AlbumListView(TemplateView):
    template_name = 'list.html'
    title = "Some Albums"

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        context['table'] = AlbumTable(Album.objects.all())
        return context
