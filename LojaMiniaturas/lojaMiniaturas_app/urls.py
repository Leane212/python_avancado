from lojaMiniaturas_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('aloja/', views.aloja, name = 'aloja'),
    path('regras/', views.regras, name = 'regras'),
    path('add_produtos/', views.add_produtos, name = 'add_produtos'),
    path('contato/', views.contato, name = 'contato')
]