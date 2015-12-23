# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('music.urls', namespace='music'))
]

try:
    user, created = User.objects.get_or_create(username='admin')
    if created:
        user.set_password('admin')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("Created admin/admin")
except:
    pass
