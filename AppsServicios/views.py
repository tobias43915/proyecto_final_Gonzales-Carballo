# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context, loader
from AppsServicios.models import Servicios,Tecnologias

#Views para el inicio

def inicio(request):

    return render(request, "AppsServicios/inicio.html")

#Lista de tecnologias

def listar_tecnologias(request):
    queryset = Tecnologias.objects.all()
    diccionario={'AppsServicios': queryset}
    plantilla = loader.get_template('AppsServicios/lista_tecnologias.html')
    documento_html = plantilla.render(diccionario)
       
    return HttpResponse(documento_html)