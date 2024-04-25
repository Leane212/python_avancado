from django.shortcuts import render
from lojaMiniaturas_app.forms import ContatoForm, ProdutoForm
from lojaMiniaturas_app.models import MensagemContato, Produto, Imagem
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect



def home (request):
    produtos = Produto.objects.order_by('id')
    #imagem = Imagem.objects.order_by('id')
    context = {'produtos': produtos}
    return render(request, 'base.html', context)

def sobre(request):
    return render(request, 'sobre.html')

def regras(request):
    return render(request, 'regras.html')

def contato(request):
    return render(request, 'contato.html')

def add_produtos(request):
    if request.method == "GET":
        form = ProdutoForm()
    else:
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {'form':form}
    return render(request,'add_produtos.html',context)

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():

            mensagem = MensagemContato(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                assunto=form.cleaned_data['assunto'],
                mensagem=form.cleaned_data['mensagem']
            )
            mensagem.save()
            return redirect('home')  
    else:
        form = ContatoForm()
    
    return render(request, 'contato.html', {'form': form})