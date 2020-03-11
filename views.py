from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import linhnhixinhdep

def surveyDisplay(request):
    return render(request, 'display.html')

def surveyProcess(request):
    linhnhixinhdep(choiceDay = request.POST['day'],
        choiceTime = request.POST['time'],
        voterName = request.POST['name'],).save()
    return HttpResponseRedirect('results')

def surveyResults(request):
    votes = linhnhixinhdep.objects.all()
    context = {'votes': votes}
    return render(request, 'results.html', context)

