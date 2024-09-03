# Create your views here.
from django.shortcuts import redirect, render

from .forms import AlunoForm
from .models import Aluno


def cadastrar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
            return redirect("listagem_alunos")
        
    elif request.method == "GET":
        form = AlunoForm()
    return render(request, "cadastro.html", {"form": form})


def listagem_alunos(request):
    alunos = Aluno.objects.all()

    return render(request, "home.html", {"alunos": alunos})
