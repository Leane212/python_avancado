from multiprocessing import context
from django.shortcuts import render
from lojaMiniaturas_app.models import *


def home(request):
    return render(request, 'base.html')

def carro (request):
    carros = Carro.objects.order_by('id')
    context - {'carros': carros}
    return render(request, 'index.html', context)

def boneca (request):
    boneca = Boneca.objects.order_by('id')
    context - {'boneca': boneca}
    return render(request, 'base.html', context)

def funkoPop (request):
    funcoPop = FunkoPop.objects.order_by('id')
    context - {'funcopop': funkoPop}
    return render(request, 'base.html', context)

