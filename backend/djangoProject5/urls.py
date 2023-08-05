from django.contrib import admin
from rest_framework.routers import SimpleRouter
from main.views import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/word/<str:word>', WordViewSet.as_view(), name='words'),
    path('api/country_info', CountryInfoViewSet.as_view(), name='countryInfos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


