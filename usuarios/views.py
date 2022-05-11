from dataclasses import field
from re import template
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

class UsuarioCreate(CreateView):
    template_name = 'usuarios/cadastro.html'
    model = User
    fields = ['username', 'email', 'password']