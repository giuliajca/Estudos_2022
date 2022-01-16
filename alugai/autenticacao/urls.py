from django.urls import path
from . import views

urlpatterns = [
    #PATH SERVE PRA CRIAR URL
    path('cadastro/', views.cadastro, name='Cadastro')

]