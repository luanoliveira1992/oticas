# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from Item.models import *
from Item.form import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView


class ConsultarMarca(ListView):
    queryset = Marca.objects.all()
    template_name = 'marca/marca.html'
    model = Marca
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        
        context = super(ConsultarMarca, self).get_context_data(**kwargs)
        numero = context['page_obj'].paginator.num_pages
        paginas = []
        for i in range(1,numero+1):
            paginas.append(i)
        
        context['localURL'] = '/marca/'
        context['CREATEACTION'] = "/marca/novo"
        context['TITULO'] = "Cadastro de Marcas de Itens"
        context['SUBTITULO'] = "Informações Sobre Marcas"
        context['DETALHAR'] = 'detalhemarca'
        context['ATUALIZAR'] ='detalhemarca'
        context['DELETAR'] = 'detalhemarca'
        context['paginas'] = paginas;
        
        
        return context
    
class InserirMarca(CreateView):
    template_name = 'marca/novaMarca.html'
    form_class = MarcaForm
    
    def salve(self, **kwargs):
        if request.method == 'POST':
            form = MarcaForm(self.request.POST)
            if(form.is_valid()):
                form.save()
                messages.success(self.request, 'Marca Inserida Com sucesso !')
            else:
                messages.error(self.request, 'É preciso informar todos os campos !')
                return render_to_response('marca/marca.html',dadosConsultar)
        
    
    def get_context_data(self, **kwargs):
        context = super(InserirMarca, self).get_context_data(**kwargs)
        context['model'] = "Marca"
        context['epigrafo'] = "Informe Todos os Campos"
        context['acaovoltar'] = "marca"
        return context
    
    def get_success_url(self):
        return "/marca/"
    
class DetalharMarca(DetailView):
    template_name = 'marca/detalheMarca.html'
    model = Marca
    
    def get_success_url(self):
        return reverse('marca')
    
    def get_context_data(self, **kwargs):
        context = super(DetalharMarca, self).get_context_data(**kwargs)
        return context
    
    

    
