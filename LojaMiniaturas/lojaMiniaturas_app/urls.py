from lojaMiniaturas_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('regras/', views.regras, name = 'regras'),
    path('add_produtos/', views.add_produtos, name = 'add_produtos'),
    path('cadastrar_categorias/', views.cadastrar_categorias, name = 'cadastrar_categorias'),
    path('cadastrar_marcas/', views.cadastrar_marcas, name = 'cadastrar_marcas'),
    path('contato/', views.contato, name = 'contato'),
    path('login/',  views.login, name = 'login'),
    path('logout/',  views.logout, name = 'logout'),
    path('cadastrouser/',  views.cadastrouser, name = 'cadastrouser'),
    path('promocao', views.promocao, name = 'promocao'),
    path('novidades', views.novidades, name = 'novidades'),
    path('deluser/<id>', views.deluser, name='deluser'),
    path('editperfil/', views.editperfil, name='editperfil'),
    path('painel/', views.painel, name='painel'),
    path('caduser/', views.caduser, name="caduser"),
    path('toggleactive/<id>', views.toggleactive, name="toggleactive"),
    path('grupos/', views.cadastrar_grupos, name="grupos"),
    path('editar_usuario/<id>', views.editar_usuario, name="editar_usuario"),
    path('editar_usuario_painel/<id>', views.editar_usuario_painel, name="editar_usuario_painel"),
    path("remover_usuario/<id>",views.remover_usuario, name="remover_usuario")
]
