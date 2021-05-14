from django.contrib import admin
from django.urls import path, include

from Atracoes import urls as Atracoes_urls
from PontoTuristico import urls as PontoTuristico_urls
from Comentarios import urls as Comentarios_urls
from Avaliacoes import urls as Avaliacoes_urls
from Localizacoes import urls as Localizacoes_urls
#restFramework ->
from rest_framework import routers
from PontoTuristico.api.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico',PontoTuristicoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
