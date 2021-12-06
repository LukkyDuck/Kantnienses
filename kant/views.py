from django.http import HttpResponse
from django.template import Template, Context, context
from django.template.loader import get_template
from django.shortcuts import render

def test1(request):

    return render(request, "test1.html")
def test2(request):
    
    return render(request, "test2.html")
    
def cuestionarioC(request):
    
    return render(request, "Cuestionario/cuestionarioC.html")

def cognitivo(request):
    
    return render(request, "Cuestionario/cognitivo.html")

def corporal(request):
    
    return render(request, "Cuestionario/corporal.html")

def ambos(request):
    
    return render(request, "Cuestionario/ambos.html")
