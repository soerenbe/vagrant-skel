# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

Menu.add_item("music", MenuItem("Index", reverse("music:index")))
Menu.add_item("music", MenuItem("Album", reverse("music:album-list"), separator=True))
Menu.add_item("music", MenuItem("Title", reverse("music:title-list")))
Menu.add_item("music", MenuItem("Artist", reverse("music:artist-list")))
Menu.add_item("music", MenuItem("Admin", reverse("admin:index"), separator=True))
