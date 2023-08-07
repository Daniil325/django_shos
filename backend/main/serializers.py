from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from main.models import *


class WordsSerializer(ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'


class CountryInfoSerializer(ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = '__all__'



class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
