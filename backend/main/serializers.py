from rest_framework.serializers import ModelSerializer
from backend.main.models import Words


class WordsSerializer(ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'
