from lojaMiniaturas_app.forms import CategoriaForm, ContatoForm, MarcaForm, ProdutoForm, LoginForm, CadastroUsuario
from lojaMiniaturas_app.models import Desconto, MensagemContato, Produto, Imagem
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User 
from django.contrib.auth.models import Permission, Group


def home (request):
    produtos = Produto.objects.order_by('id')
    #imagem = Imagem.objects.order_by('id')
    if request.user.is_authenticated:
        context = {'produtos': produtos, 'formulario': LoginForm(), 'formcadastro': CadastroUsuario(instance=User.objects.get(id=request.user.id))}
    else:
        context = {'produtos': produtos, 'formulario': LoginForm(), 'formcadastro': CadastroUsuario()}
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
            form = form.save()
            imagem = Imagem.objects.create(name = request.POST["imagem"], id_produto = form.id)
            imagem.save()
            return HttpResponseRedirect(reverse('home'))
    context = {'form':form}
    return render(request,'add_produtos.html',context)

def cadastrar_categorias(request):
    if request.method == "GET":
        form = CategoriaForm()
    else:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'cadastrar_categorias.html', context)


def cadastrar_marcas(request):
    if request.method == "GET":
        form = MarcaForm()
    else:
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'cadastrar_marcas.html', context)

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

def formulario(request):
    return render (request, 'index.html', {'forms': LoginForm()})

def login (request):
    if request.method == 'POST':
        #fazer o login
       user = authenticate(username = request.POST.get('username'),
                        password =request.POST.get('password'))
       if user:
           auth_login(request, user)
    return HttpResponseRedirect(reverse('home'))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def cadastrouser(request):
    if request.method == 'POST':
        form = CadastroUsuario (request.POST)
        if form.is_valid():
            if request.POST.get('password') != request.POST.get('confirmacao'):
                form.add_error('password', 'As senhas devem ser iguais.')
            else:
                permlist = []
                for permissao in request.POST.getlist("permissao"):
                    permlist.append(Permission.objects.get(id=permissao))
                    
                form = form.save(commit=False)
                form.password = make_password(form.password)
                form.save()
                
    form = CadastroUsuario()
    contexto = {"form":form}
    return render(request,"cadastro.html",contexto)
    # return HttpResponseRedirect(reverse('home'))

def promocao (request):
    promocoes = Desconto.objects.order_by('data_inicial')[:10]
    context = {'promocoes': promocoes}
    return render(request, 'promocao.html', context)
    #{{promocoes.produto.nome}}
    #{{promocoes.valor}}

def novidades (request):
    novidade = Produto.objects.order_by('-data_cadastro')[:2]
    context = {'novidade': novidade}
    return render(request, 'novidades.html', context)

def deluser (request, id):
    user = User.objects.get(id=id)
    user.delete()
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def editperfil (request):
    if request.method == 'POST':
        print(request.user)
        usuario = User.objects.get(id=request.user.id)
        novo_usuario = request.POST.copy()
        novo_usuario['password'] = usuario.password
        novo_usuario['username'] = usuario.username
        user = CadastroUsuario(instance=usuario, data=novo_usuario)
        if user.is_valid:
            user.save()
            
        ''' permlist = []
            for permissao in request.POST.getlist("permissao"):
                permlist.append(Permission.objects.get(id=permissao))
            user = user.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            user.user_permissions.set(permlist)'''
            
    return HttpResponseRedirect(reverse('home'))

def adm(request):
    if request.method == "GET" and request.user.is_superuser:
        usuarios = User.objects.all;
        contexto = {"usuarios":usuarios}
        return render(request, "adm.html", contexto)
    return HttpResponseRedirect(reverse('home'))

def alternaractive(request,id):
    usuario = User.objects.get(id = id)
    usuario.is_active = not usuario.is_active
    usuario.save()
    return HttpResponseRedirect(reverse("adm"))

#CRIAR
# #def Usuario (user):
    cpf = models.TextField()

def alternarsuperuser(request,id):
    usuario = User.objects.get(id = id)
    usuario.is_superuser = not usuario.is_superuser
    usuario.save()
    return HttpResponseRedirect(reverse("adm"))


def alternarstaff(request,id):
    usuario = User.objects.get(id = id)
    usuario.is_staff = not usuario.is_staff
    usuario.save()
    return HttpResponseRedirect(reverse("adm"))

# esse é o def painel do professor
def admusuario(request,id):
    #ver ta altenticado e se é superuser 
    if request.method == 'GET' and request.user.is_authenticated and request.user.is_superuser:
     permissoes = Permission.objects.order_by('id')
    permissoes_agrupadas = {}
    for permissao in permissoes:
        objeto = permissao.codename.split("_")
        if objeto[1] not in permissoes_agrupadas:
            permissoes_agrupadas[objeto[1]] = {permissao.name : permissao.id}
        else:
            permissoes_agrupadas[objeto[1]][permissao.name] = permissao.id
            
        
    usuario = User.objects.get(id=id)
    form_cadastro = CadastroUsuario(instance=usuario)
    contexto = {
    "usuario":usuario,
    "permissoes":permissoes_agrupadas,
    "formcadastro":form_cadastro,
    "grupos": Group.objects.all(),
    }
    
    return render(request,"admusuario.html",contexto)

