from django.db import models


class Words(models.Model):
    word = models.CharField("Слово", max_length=500)
    definition = models.CharField(max_length=500)
    associations = models.JSONField()
    synonyms = models.JSONField()
    examples = models.JSONField()
    image_link = models.CharField(max_length=500)

    def __str__(self):
        return self.word


class Country(models.Model):
    name = models.CharField("Страна", max_length=500)

    def __str__(self):
        return self.name


class CountryInfo(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    president = models.CharField("Президент", max_length=500)
    capital = models.CharField("Столица", max_length=500)
    language = models.CharField("Язык", max_length=500)
    valuta = models.CharField("Валюта", max_length=500)

    def __str__(self):
        return self.president
