# Create your views here.
from contextlib import redirect_stderr
from ensurepip import version
from typing import Dict
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.template import Template,Context, loader
from AppsServicios.models import Tecnologias
from AppsServicios.models import Contactos
from AppsServicios.models import Servicios
from AppsServicios.forms import TecnologiaFormulario,ContactosFormulario
from AppsServicios.forms import ServicioFormulario

#Views para el inicio

def inicio(request):

    return render(request, "AppsServicios/inicio.html")

#------------------------------------------Views tecnologias------------------------------#

def listar_tecnologias(request):
    queryset = Tecnologias.objects.all()
    diccionario={'AppsServicios': queryset}
    plantilla = loader.get_template('lista_tecnologias.html')
    documento_html = plantilla.render(diccionario)
       
    return HttpResponse(documento_html)

def tecnologia(request):
    tecnologia = Tecnologias.objects.all()
    #--------------------------nuevo 1709-----------------------------
    borrado = request.GET.get('borrado', None)
    contexto= {'tecnologia':tecnologia}
    contexto ['borrado'] = borrado
    return render(request, "AppsServicios/lista_tecnologias.html",contexto)

def tecnologia_formulario(request):
    if request.method == 'POST':
        formulario = TecnologiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            tecnologia = Tecnologias(nombre=data['nombre'], version=data['version'])
            tecnologia.save()
            return render(request, 'AppsServicios/inicio.html', {"exitoso": True})
    else:  # GET
        formulario = TecnologiaFormulario()  
    return render(request, 'AppsServicios/form_tecnologias.html', {"formulario": formulario})

#-------------------------busqueda---------------------------------
def busqueda_tecnologia_form(request):
      return render(request, "AppsServicios/form_buscar.html")

def buscar(request):
      if request.GET["tecnologia"]:
            tecnologia = request.GET["tecnologia"]
            tecnologia = Tecnologias.objects.filter(tecnologia__icontains=tecnologia)
            return render(request, "AppsServicios/inicio.html", {'tecnologia': tecnologia})
      
      else:

        respuesta= "No ingresaste informacion"
        
        return render(request, "AppsServicios/inicio.html", {'respuesta':respuesta})

#-------------------------------------------nuevo 1709 elimina tecno-----------------------

def eliminar_tecnologia(request, id):
    tecnologia = Tecnologias.objects.get(id=id)
    borrado_id = tecnologia.id
    tecnologia.delete()
    url_final = f"{reverse('tecnologias')}?borrado={borrado_id}"
    return redirect(url_final)

#E-----------------------------ditar las tecnologias 1709----------------------------------------

def editar_tecnologia(request, id):

    tecnologia = Tecnologias.objects.get(id=id)

    if request.method == 'POST':
        formulario = TecnologiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            tecnologia.nombre = data['nombre']
            tecnologia.version = data['version']
            tecnologia.save()

            return redirect(reverse('tecnologias'))

    else:  # GET
        inicial = {
            'nombre': tecnologia.nombre,
            'version': tecnologia.version,
        }
        formulario = TecnologiaFormulario(initial=inicial)
    return render(request, 'AppsServicios/form_tecnologias.html', {"formulario": formulario})

#----------------------------------Views servicios------------------------------------------------------#

def servicio(request):
    servicio = Servicios.objects.all()    
    borrado = request.GET.get('borrado', None)
    contexto= {'servicio':servicio}
    contexto ['borrado'] = borrado
    return render(request, "AppsServicios/lista_servicios.html",contexto)
    
#---------------------form servicio--------------------------

def servicio_formulario(request):
    if request.method == 'POST':
        formulario = ServicioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            servicio = Servicios(nombre=data['nombre'], valor=data['valor'],tiempo=data['tiempo'])
            servicio.save()
            return render(request, 'AppsServicios/inicio.html', {"exitoso": True})
    else:  # GET
        formulario = ServicioFormulario()  
    return render(request, 'AppsServicios/form_servicios.html', {"formulario": formulario})

#----------------------------eliminar servicio-----------------

def eliminar_servicio(request, id):
    servicio = Servicios.objects.get(id=id)
    borrado_id = servicio.id
    servicio.delete()
    url_final = f"{reverse('servicios')}?borrado={borrado_id}"
    return redirect(url_final)
#------------------------editar servicios------------------

def editar_servicio(request, id):

    servicio = Servicios.objects.get(id=id)

    if request.method == 'POST':
        formulario = ServicioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            servicio.nombre = data['nombre']
            servicio.valor = data['valor']
            servicio.tiempo = data['tiempo']
            servicio.save()

            return redirect(reverse('servicios'))

    else:  # GET
        inicial = {
            'nombre': servicio.nombre,
            'valor': servicio.valor,
            'tiempo': servicio.tiempo,
        }
        formulario = ServicioFormulario(initial=inicial)
    return render(request, 'AppsServicios/form_servicios.html', {"formulario": formulario})

#---------------------------------views contactos------------------------------------------------------#

def contacto(request):
    contacto = Contactos.objects.all()
    borrado = request.GET.get('borrado', None)
    contexto= {'contacto':contacto}
    contexto ['borrado'] = borrado
    return render(request, "AppsServicios/contactos.html",contexto)

def contacto_formulario(request):
    if request.method == 'POST':
        formulario = ContactosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            contacto = Contactos(nombre=data['nombre'], apellido=data['apellido'],email=data['email'])
            contacto.save()
            return render(request, 'AppsServicios/inicio.html', {"exitoso": True})
    else:  # GET
        formulario = ContactosFormulario()  
    return render(request, 'AppsServicios/form_contacto.html', {"formulario": formulario})

#--------------------------------------eliminar contacto------------------

def eliminar_contacto(request, id):
    contacto = Contactos.objects.get(id=id)
    borrado_id = contacto.id
    contacto.delete()
    url_final = f"{reverse('contactos')}?borrado={borrado_id}"
    return redirect(url_final)

#----------------editar---------------

def editar_contacto(request, id):

    contacto = Contactos.objects.get(id=id)

    if request.method == 'POST':
        formulario = ContactosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            contacto.nombre = data['nombre']
            contacto.apellido = data['apellido']
            contacto.email = data['email']
            contacto.save()

            return redirect(reverse('contactos'))

    else:  # GET
        inicial = {
            'nombre': contacto.nombre,
            'apellido': contacto.apellido,
            'apellido': contacto.email,
        }
        formulario = ContactosFormulario(initial=inicial)
    return render(request, 'AppsServicios/form_contacto.html', {"formulario": formulario})

