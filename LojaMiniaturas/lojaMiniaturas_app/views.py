from django.shortcuts import render
from lojaMiniaturas_app.forms import CategoriaForm, ContatoForm, FormGrupo, MarcaForm, ProdutoForm, LoginForm, CadastroUsuario
from lojaMiniaturas_app.models import Desconto, MensagemContato, Produto, Imagem, Usuario
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Permission, Group

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
            imagem = Imagem.objects.create(name = request.POST["imagem"], pr = form.id)
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

def cadastrar_grupos(request):
    if request.method == "GET":
        form = FormGrupo()
    else:
        form = FormGrupo(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'grupos.html', context)

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

def cadastro_Usuario(request):
    user = CadastroUsuario(request.POST,auto_id=False)
    if user.is_valid():
        if user.data.get('password') != user.data.get('confirmacao'):
            user.add_error('password', 'As senhas devem ser iguais.')
        else:
            user = user.save(commit=False)
            user.password = make_password(user.password)
            user.save()
    return user

def cadastrouser(request):
    if request.method == 'POST':
        form = CadastroUsuario (request.POST)
        if form.is_valid():
            if request.POST.get('password') != request.POST.get('confirmacao'):
                form.add_error('password', 'As senhas devem ser iguais.')
            else:
                form = form.save(commit=False)
                form.password = make_password(form.password)
                form.save()
    return HttpResponseRedirect(reverse('home'))


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
    return HttpResponseRedirect(reverse('home'))


def caduser (request):
    if request.method == 'POST' and request.user.is_superuser:
        user = cadastro_Usuario(request)
        permlist = []
        for permissao in request.POST.getlist("permissao"):
                permlist.append(Permission.objects.get(id=permissao))
        user.user_permissions.set(permlist)

        grupos = []
        for grupo in request.POST.getlist("grupo"):
                grupos.append(Group.objects.get(id=grupo))
        print(grupos)
        user.groups.set(grupos)

        return HttpResponseRedirect(reverse('painel'))
    return HttpResponseRedirect(reverse('home'))


def painel (request):
    if request.method == 'GET' and request.user.is_superuser:
        permissoes = Permission.objects.order_by('id')
        permissoes_agrupadas = {}
        for permissao in permissoes:
            objeto = permissao.codename.split("_")
            if objeto[1] not in permissoes_agrupadas:
                permissoes_agrupadas[objeto[1]] = {objeto[0] : permissao.id}
            else:
                permissoes_agrupadas[objeto[1]][objeto[0]] = permissao.id
        contexto = context(request)
        contexto['formcadastro'] = CadastroUsuario()
        contexto['permissoes'] = permissoes_agrupadas
        contexto['grupos'] = Group.objects.all()
        contexto['users'] = Usuario.objects.order_by('first_name')
        return render(request,'painel.html',contexto)
    return HttpResponseRedirect(reverse('home'))

def context (request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user_ptr_id = request.user.id)
        request.user.matricula = usuario.matricula
        request.user.cpf = usuario.cpf
        return {
            'formcadastro':CadastroUsuario(instance=usuario),        #perfil
        }
    else:
        return {
            'formulario':LoginForm(),                          #login
        }
    
def toggleactive (request,id):
    if request.method == 'GET' and request.user.is_superuser:
        usuario = Usuario.objects.get(user_ptr_id=id)
        usuario.is_active = not usuario.is_active
        usuario.save()
        return HttpResponseRedirect(reverse('painel'))
    return HttpResponseRedirect(reverse('index'))


def editar_usuario(request, id):
    
    if request.user.is_authenticated and request.user.is_superuser:
        permissoes = Permission.objects.order_by('id')
        permissoes_agrupadas = {}
        for permissao in permissoes:
            objeto = permissao.codename.split("_")
            if objeto[1] not in permissoes_agrupadas:
                permissoes_agrupadas[objeto[1]] = {objeto[0]: permissao.id}
            else:
                permissoes_agrupadas[objeto[1]][objeto[0]] = permissao.id

        usuario = User.objects.get(id=id)
        form_usuario = CadastroUsuario(instance=usuario)
        permissoes_usuario = usuario.user_permissions.values_list('id', flat=True)

        contexto = {
            "usuario": usuario,
            "permissoes": permissoes_agrupadas,
            "form_usuario": form_usuario,
            "grupos": Group.objects.all(),
            "permissoes_usuario": permissoes_usuario,
        }

        return render(request, "editar_usuario.html", contexto)
    else:
        return HttpResponseRedirect(reverse("home"))
    
def editar_usuario_painel(request, id):
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_superuser:
        usuario = User.objects.get(id=id)
        novo_usuario = request.POST.copy()
        novo_usuario["password"] = usuario.password  # Keep the existing password
        user_form = CadastroUsuario(instance=usuario, data=novo_usuario)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.password = usuario.password  
            user.save()

            # Prepare the permission list
            permlist = []
            permissoes = request.POST.getlist("permissoes")
            for permissao in permissoes:
                permlist.append(Permission.objects.get(id=permissao))

            user.user_permissions.set(permlist)
            user.save()

            return HttpResponseRedirect(reverse('painel'))
        else:
            permissoes = Permission.objects.order_by('id')
            permissoes_agrupadas = {}
            for permissao in permissoes:
                objeto = permissao.codename.split("_")
                if objeto[1] not in permissoes_agrupadas:
                    permissoes_agrupadas[objeto[1]] = {objeto[0]: permissao.id}
                else:
                    permissoes_agrupadas[objeto[1]][objeto[0]] = permissao.id

            permissoes_usuario = usuario.user_permissions.values_list('id', flat=True)

            contexto = {
                "usuario": usuario,
                "permissoes": permissoes_agrupadas,
                "form_usuario": user_form,
                "grupos": Group.objects.all(),
                "permissoes_usuario": permissoes_usuario,
            }
            return render(request, "editar_usuario.html", contexto)

    return HttpResponseRedirect(reverse('home'))

def remover_usuario(request,id):
    if request.user.is_authenticated and request.user.is_superuser:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect(reverse("painel"))
    
    return HttpResponseRedirect(reverse("home"))
    
def remover_produto(request,id):
    if request.user.is_authenticated and request.user.is_superuser:
        produto = Produto.objects.get(id=id)
        produto.delete()
        return HttpResponseRedirect(reverse("add_produto"))
    
    return HttpResponseRedirect(reverse("home"))
    