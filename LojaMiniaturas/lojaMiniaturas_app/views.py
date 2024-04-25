from django.shortcuts import render
from lojaMiniaturas_app.models import Produto, Imagem



def home (request):
    # produto = Produto.objects.order_by('id')
    produto = Imagem.objects.order_by('id')
    context = {'produto': produto}
    return render(request, 'base.html', context)

def sobre(request):
    return render(request, 'sobre.html')

def regras(request):
    return render(request, 'regras.html')