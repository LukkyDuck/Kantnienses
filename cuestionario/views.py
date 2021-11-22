from django.shortcuts import render

from cuestionario.forms import MoodForm

# Create your views here.

def quest(request):
    context = {}
    form = MoodForm
    context['form'] = form
    if request.GET:
        temp = int(request.GET['mood_field'])
        temp += int(request.GET['mood1_field'])
        print(temp)
        if temp == 2:
            return render(request, "Cuestionario/bien.html")
        elif temp >= 3:
            return render(request, "Cuestionario/masomenos.html")
    return render(request,"Cuestionario/cuestionario.html", context)
