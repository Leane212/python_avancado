from lojaMiniaturas_app import views
from django.urls import path

urlpatterns = [
    path('', views.home),
]
