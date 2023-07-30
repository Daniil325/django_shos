from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from backend.main.views import WordViewSet

router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/word/<str:word>', WordViewSet.as_view(), name='words')
]


