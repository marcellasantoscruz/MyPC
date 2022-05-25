from django.urls import path

from perg_resp.views import *

urlpatterns = [
    path('processador-iniciante/', processadorIniciante, name='processador_iniciante'),
]