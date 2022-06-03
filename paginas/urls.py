from django.urls import path
from .views import PaginaInicial, Modulos

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('modulos/', Modulos, name='modulos'),
]