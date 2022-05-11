from unicodedata import name
from django.urls import path
from .views import PaginaInicial, Modulos

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('modulos/', Modulos.as_view(), name='modulos'),
]