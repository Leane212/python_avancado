from django import forms
from lojaMiniaturas_app.models import MensagemContato, Produto, Imagem
from django.forms.widgets import *
from django.contrib.auth.models import User


class ProdutoForm (forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','descricao','codigo','video','data_cadastro','marca','categoria','especificacao']
        labels = {'preco':"Preço"}
        
    def _init_ (self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
            {'placeholder':'Nome do produto',
            'class' : 'form-control'}
        )
        self.fields['preco'].widget.attrs.update(
            {'placeholder':'Preço',
            'class' : 'form-control'}
        )
        self.fields['descricao'].widget.attrs.update(
            {'placeholder':'Descrição',
            'class' : 'form-control'}
        )
        self.fields['codigo'].widget.attrs.update(
            {'placeholder':'Código',
            'class' : 'form-control'}
        )
        self.fields['video'].widget.attrs.update(
            {'placeholder':'Video',
            'class' : 'form-control'}
        )
        self.fields['data_cadastro'].widget.attrs.update(
            {'placeholder':'Data do Cadastro',
            'class' : 'form-control'}
        )
        self.fields['marca'].widget.attrs.update(
            {'placeholder':'Marca do produto',
            'class' : 'form-control'}
        )
        self.fields['categoria'].widget.attrs.update(
            {'placeholder':'Categoria',
            'class' : 'form-control'}
        )
        self.fields['especificacao'].widget.attrs.update(
            {'placeholder':'Especificações do Produto',
            'class' : 'form-control'}
        )

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['nome']     
    
    def _init_ (self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
            {'placeholder':'Nome da imagem',
            'class' : 'form-control'}
        )
        
class ContatoForm(forms.Form):
    class Meta: 
        model= MensagemContato
        fields = ['nome','email','assunto','mensagem']

    def _init_ (self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
            {'placeholder':'Seu Nome',
            'class' : 'form-control'}
        )
        self.fields['email'].widget.attrs.update(
            {'placeholder':'Seu E-mail',
            'class' : 'form-control'}
        )
        self.fields['assunto'].widget.attrs.update(
            {'placeholder':'assunto',
            'class' : 'form-control'}
        )
        self.fields['mensagem'].widget.attrs.update(
            {'placeholder':'Mensagem',
            'class' : 'form-control'}
        )
        
    nome = forms.CharField(label='Seu Nome', max_length=100)
    email = forms.EmailField(label='Seu E-mail')
    assunto = forms.CharField(label='Assunto', max_length=255)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

class LoginForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'password']
        widgets = {'passoword': PasswordInput()}
            
    def _init_ (self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'placeholder':'Nome Usuário',
        'class' : 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
        {'placeholder':'Senha',
        'class' : 'form-control'}
        )

class CadastroUsuario (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'email': EmailInput(), 'password': PasswordInput()}

    def _init_ (self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'placeholder':'Nome Usuário',
        'class' : 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
        {'placeholder':'Senha',
        'class' : 'form-control'}
        )
        self.fields['email'].widget.attrs.update(
        {'placeholder':'Email',
        'class' : 'form-control'}
        )
        self.fields['first_name'].widget.attrs.update(
        {'placeholder':'Primeiro Nome',
        'class' : 'form-control'}
        )
        self.fields['last_name'].widget.attrs.update(
        {'placeholder':'Segundo Nome',
        'class' : 'form-control'}
        )