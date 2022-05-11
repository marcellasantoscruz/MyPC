from re import template
from django.views.generic import TemplateView

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'