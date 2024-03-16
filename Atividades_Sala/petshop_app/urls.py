from django.urls import path
from petshop_app import views

urlpatterns = [
    path('', views.home),
]
