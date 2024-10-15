from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def primera_vista(request):
    return HttpResponse("Primera Prueba de Vista")

def home(request):
    return HttpResponse("Pagina inicio")

def vista2(requested, dato):
    datoURL = dato
    return HttpResponse(f"El dato del URL es : {datoURL} ")

def template_1(request):
    # return HttpResponse("TEMPLATE_1")
    template_1_file = open(r".venv\templates\template_1.html")
    template = Template(template_1_file.read())
    template_1_file.close()
    contexto = Context()
    render_template = template.render(contexto)
    return HttpResponse(render_template)