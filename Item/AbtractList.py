from django.db import models
class ConsultarModel(ListView):
    
    queryset = self.model.objects.all()
    template_name = template
    model = self.model
    paginate_by = pageNumber
    
    def __init__(self, model, template,pageNumber):
        self.model = model
        self.template = template
        self.pageNumber = pageNumber
    
    def get_context_data(self, **kwargs):
        
        context = super(ConsultarModel, self).get_context_data(**kwargs)
        numero = context['page_obj'].paginator.num_pages
        paginas = []
        for i in range(1,numero+1):
            paginas.append(i)
        
        context['localURL'] = self.localUrl
        context['CREATEACTION'] = self.createAction
        context['TITULO'] = self.titulo
        context['SUBTITULO'] = self.subTitulo
        context['DETALHAR'] = self.detalhe
        context['ATUALIZAR'] = self.atualizar
        context['DELETAR'] = deletar
        context['paginas'] = paginas;
        
        
        return context
    
    def localURL(self, localUrl):
        self.localUrl = localUrl
    
    def createAction(self, create):
        self.createAction = create
   
    
    def titulo(self, titulo):
        self.titulo = titulo
    
    def subTitulo(self, subTitulo):
        self.subTitulo = subTitulo
    
    def detalhar(self, detalhe):
        self.detalhe = detalhe
    
    def atualizar(self, atualizar):
        self.atualizar = atualizar
    
    def deletar(self, deletar):
        self.deletar = deletar
    
    def paginas(self, paginas):
        self.paginas = paginas