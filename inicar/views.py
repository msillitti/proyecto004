from django.shortcuts import render
from django.http import HttpResponse

def primera_vista(request):
    retrun HttpResponse("Primera Prueba de Vista")

def home(request):
    return HttpResponse(<h1 style="text-align:center;font-family:Garamond;color:#000000;">Matias Sillitti Primera Vista</h1>)

# Create your views her