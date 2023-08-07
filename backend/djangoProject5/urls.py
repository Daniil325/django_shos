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
    path('api/news', NewsViewSet.as_view(), name='news'),
    path('api/news/<int:post_id>', NewsByIdViewSet.as_view(), name='news_by_id'),
    path('api/news_by_country/<int:country_id>', NewsByCountryViewSet.as_view(), name='news_by_country'),
    path('ckedotor/', include('ckeditor_uploader.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


