from lojaMiniaturas_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('regras/', views.regras, name = 'regras'),
    path('add_produtos/', views.add_produtos, name = 'add_produtos'),
    path('contato/', views.contato, name = 'contato')
]