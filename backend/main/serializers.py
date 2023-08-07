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
    image_url = serializers.SerializerMethodField('get_img_url')

    class Meta:
        model = News
        fields = '__all__'

    def get_img_url(self, obj):
        print(obj.post_image.url.replace("3001", "8000"))
        return 'http://localhost:8000/media/'+ obj.post_image.url