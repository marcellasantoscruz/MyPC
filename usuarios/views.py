from dataclasses import field
from re import template
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

# class NomeClasse(LoginRequiredMixin):
#     login_url = reverse_lazy('login')

class UsuarioCreate(CreateView):
    template_name = 'usuarios/cadastro.html'
    model = User
    fields = ['username', 'email', 'password']