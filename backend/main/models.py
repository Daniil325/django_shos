from django.db import models


class Words(models.Model):
    word = models.CharField("Слово", max_length=500)
    definition = models.CharField(max_length=500)
    associations = models.JSONField()
    synonyms = models.JSONField()
    examples = models.JSONField()
    image_link = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self):
        return self.word


class Country(models.Model):
    name = models.CharField("Страна", max_length=500)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class CountryInfo(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    president = models.CharField("Президент", max_length=500)
    capital = models.CharField("Столица", max_length=500)
    language = models.CharField("Язык", max_length=500)
    valuta = models.CharField("Валюта", max_length=500)
    code = models.CharField("Код страны", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Информация о стране'
        verbose_name_plural = 'Информация о странах'

    def __str__(self):
        return self.president


class News(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    header = models.CharField("Заголовок", max_length=500)
    message = models.TextField()
    pub_date = models.DateField()
    post_image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

