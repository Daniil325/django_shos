from rest_framework.serializers import ModelSerializer
from main.models import Words, CountryInfo


class WordsSerializer(ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'


class CountryInfoSerializer(ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = '__all__'
