from django.shortcuts import render
from lojaMiniaturas_app.models import Produto



def home (request):
    produto = Produto.objects.order_by('id')
    context = {'produto': produto}
    return render(request, 'base.html', context)

def aloja(request):
    return render(request, 'aloja.html')

def regras(request):
    return render(request, 'regras.html')