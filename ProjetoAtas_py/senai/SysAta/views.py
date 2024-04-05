from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Ata

def ata(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def todasAtas(request):
    atas = Ata.objects.all().values()
    template = loader.get_template('todasAtas.html')
    context = {
        'atas': atas
    }
    return HttpResponse(template.render(context,request))
