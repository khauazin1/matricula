from django.urls import path

from . import views

urlpatterns = [
    path("", views.listagem_alunos, name="listagem_alunos"),
    path("cadastro/", views.cadastrar_aluno, name="cadastrar_alunos"), 
]