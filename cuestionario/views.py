from django.shortcuts import redirect, render

from cuestionario.forms import MoodForm

# Create your views here.

def quest(request):
    context = {}
    form = MoodForm
    context['form'] = form
    if request.GET:
        cont = int(request.GET['pregunta1'])
        cont += int(request.GET['pregunta2'])
        cont += int(request.GET['pregunta3'])
        cont += int(request.GET['pregunta4'])
        cont += int(request.GET['pregunta5'])
        cont += int(request.GET['pregunta6'])
        cont += int(request.GET['pregunta7'])
        cont += int(request.GET['pregunta8'])
        cont += int(request.GET['pregunta9'])
        cont += int(request.GET['pregunta10'])
        cont += int(request.GET['pregunta11'])
        cont += int(request.GET['pregunta12'])
        if cont >= 0:
            return redirect('cuestionarioC') 
    return render(request,"Cuestionario/cuestionario.html", context)

def quest2(request):
    return render(request, "Cuestionario/cuestionario2.html")