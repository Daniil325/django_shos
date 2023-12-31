from django.db.models import Max
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import *
from main.serializers import *
from main.pars import get_word
from main.models import CountryInfo


class WordViewSet(APIView):
    def get(self, request, *args, **kwargs):
        word = kwargs['word']
        words = Words.objects.filter(word=word)
        if words.exists():
            serializer = WordsSerializer(words, many=True)
            return Response(serializer.data)
        else:
            result = get_word(word)
            new_id = Words.objects.all().aggregate(Max('id'))

            new_word = Words(id=new_id['id__max']+1, word=word, associations=result['associations'],
                             definition=result['definition'], examples=result['examples'],
                             synonyms=result['synonyms'], image_link=result['image_link'])

            new_word.save()
            serializer = WordsSerializer(words, many=True)
            return Response(serializer.data)


class CountryInfoViewSet(APIView):
    def get(self, request):
        result = CountryInfo.objects.all()
        serializer = CountryInfoSerializer(result, many=True)
        return Response(serializer.data)


class NewsViewSet(APIView):
    def get(self, request):
        result = News.objects.all()
        serializer = NewsSerializer(result, many=True)
        return Response(serializer.data)


class NewsByIdViewSet(APIView):
    def get(self, request, *args, **kwargs):
        post_id = kwargs['post_id']
        result = News.objects.filter(id=post_id)
        serializer = NewsSerializer(result, many=True)
        return Response(serializer.data)


class NewsByCountryViewSet(APIView):
    def get(self, request, *args, **kwargs):
        country_id = kwargs['country_id']
        result = News.objects.filter(country_id=country_id)
        serializer = NewsSerializer(result, many=True)
        return Response(serializer.data)