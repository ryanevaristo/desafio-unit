from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from usuario.models import Usuario
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    return render(request, 'base.html')


class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'forms.html'
    fields = ['atividade', 'quant_horas','status','certificado']
    success_url = reverse_lazy('index')



class UsuarioUpdate(UpdateView):
    model = Usuario
    template_name = 'forms.html'
    fields = ['atividade', 'quant_horas','status','certificado']
    success_url = reverse_lazy('index')


class UsuarioDelete(DeleteView):
    model=Usuario
    template_name = 'forms-excluir.html'
    success_url = reverse_lazy('index')


class UsuarioList(ListView):
    model = Usuario
    template_name = 'index.html'
    paginate_by = 10



