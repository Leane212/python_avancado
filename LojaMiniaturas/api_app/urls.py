from api_app import views
from django.urls import path

urlpatterns = [
    path('categoria/', views.GetPostCategoriaView.as_view()),
    path('categoria/<id>', views.GetPutDeleteCategoriaView.as_view()),
    path ('produto/', views.produto),
    path ('produto/<id>', views.produto_id),
]