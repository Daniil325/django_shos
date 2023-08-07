from django.contrib import admin
from django.contrib.admin import ModelAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from django import forms


class PostAdminForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(Words)
class WordsAdmin(ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    pass


@admin.register(CountryInfo)
class CountryInfoAdmin(ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(ModelAdmin):
    form = PostAdminForm
