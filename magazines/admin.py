# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Magazine
from .models import Purchase

# Register your models here.
admin.site.register(Magazine)
admin.site.register(Purchase)
