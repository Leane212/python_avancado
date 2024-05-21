from lojaMiniaturas_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('regras/', views.regras, name = 'regras'),
    path('add_produtos/', views.add_produtos, name = 'add_produtos'),
    path('contato/', views.contato, name = 'contato'),
    path('login/',  views.login, name = 'login'),
    path('logout/',  views.logout, name = 'logout'),
    path('cadastrouser/',  views.cadastrouser, name = 'cadastrouser'),
    path('promocao', views.promocao, name = 'promocao'),
    path('novidades', views.novidades, name = 'novidades'),
    path('deluser/<id>', views.deluser, name='deluser'),
    path('editperfil/', views.editperfil, name='editperfil')
]