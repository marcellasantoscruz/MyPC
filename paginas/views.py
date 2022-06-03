from django.views.generic import TemplateView
from django.shortcuts import render
from perg_resp.models import *

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

def Modulos(request):
    registros = ProcessadorIniciante.objects.all()
    registros.delete()
    return render(request, 'paginas/modulos.html')