from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from main.views import *

router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/word/<str:word>', WordViewSet.as_view(), name='words'),
    path('api/country_info', CountryInfoViewSet.as_view(), name='countryInfos'),
]


