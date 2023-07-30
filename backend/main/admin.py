from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(Words)
class WordsAdmin(ModelAdmin):
    pass
