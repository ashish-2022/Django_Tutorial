# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Import your model
from . models import employee

# Register your models here.
admin.site.register(employee)

