from django.db import models
# -*- coding: utf-8 -*-
class Marca(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField("Descrição", max_length=255)
    observacao = models.TextField(verbose_name="Observação")
    
    def keys(self):
        return self.codigo

class ClasseItem(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField("Descrição",max_length=100)
    
    def get_absolute_url(self):
        return reverse('/marca/')

class Item(models.Model):
    
    TIPO_ITEM = (
                (0, "Material"),
                (1, "Serviço")
                )
    
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField("Nome do Item",max_length=255)
    marca = models.ForeignKey(Marca,verbose_name="Marca")
    classe = models.ForeignKey(ClasseItem, verbose_name="Categoria")
    tipo = models.IntegerField("Tipo Item",choices=TIPO_ITEM)
    
