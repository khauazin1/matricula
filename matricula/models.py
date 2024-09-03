from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=80)
    endereco = models.CharField(max_length=80)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome