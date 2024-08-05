from api_app import views
from django.urls import path

urlpatterns = [
    path('categoria/', views.categoria),
    path('categoria/<id>', views.categoria_id),
    path('produto/', views.produto),
    path('produto/<id>', views.produto_id)
]

