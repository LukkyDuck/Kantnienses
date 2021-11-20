from django.http import HttpResponse
from django.template import Template, Context, context
from django.template.loader import get_template
from django.shortcuts import render

def test1(request):

    return render(request, "test1.html")
def test2(request):
    
    return render(request, "test2.html")