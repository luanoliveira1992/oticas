# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from Item.views import * 
from Item.models import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^marca/$', ConsultarMarca.as_view(),name='marca'),
    url(r'^marca/novo/$', InserirMarca.as_view(),name='novamarca'),
    url(r'^marca/page(?P<page>[0-9]+)/$', ConsultarMarca.as_view(),name='marca'),
    url(r'^marca/detalhe/(?P<pk>\d+)/$', DetalharMarca.as_view(),name='detalhemarca'),
]
