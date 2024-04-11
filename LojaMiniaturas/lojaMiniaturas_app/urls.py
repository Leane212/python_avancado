from lojaMiniaturas_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('carro/', views.carro, name='carro'),
    path('boneca/', views.boneca, name='boneca'),
    path('funkoPop/', views.funkoPop, name='funcoPop')
]
