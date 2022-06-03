from django.urls import path

from perg_resp.views import *

urlpatterns = [
    path('proc-ini-1/', processadorIniciante1, name='processador_iniciante-1'),
    path('proc-ini-2/', processadorIniciante2, name='processador_iniciante-2'),
    path('proc-ini-3/', processadorIniciante3, name='processador_iniciante-3'),
    path('proc-ini-p1/', processadorIniciantePergunta1, name='processador_iniciante_pergunta-1'),
    path('proc-ini-p2/', processadorIniciantePergunta2, name='processador_iniciante_pergunta-2'),
    path('proc-ini-p3/', processadorIniciantePergunta3, name='processador_iniciante_pergunta-3'),
    path('proc-ini-p4/', processadorIniciantePergunta4, name='processador_iniciante_pergunta-4'),
    path('proc-ini-p5/', processadorIniciantePergunta5, name='processador_iniciante_pergunta-5'),
    path('proc-ini-p6/', processadorIniciantePergunta6, name='processador_iniciante_pergunta-6'),
    path('proc-ini-p7/', processadorIniciantePergunta7, name='processador_iniciante_pergunta-7'),
    path('proc-ini-p8/', processadorIniciantePergunta8, name='processador_iniciante_pergunta-8'),
    path('proc-ini-p9/', processadorIniciantePergunta9, name='processador_iniciante_pergunta-9'),
    path('proc-ini-p10/', processadorIniciantePergunta10, name='processador_iniciante_pergunta-10'),
    path('resultado/', resultado, name='resultado'),
]