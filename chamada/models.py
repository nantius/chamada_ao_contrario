from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.carga_horaria} horas"


class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=10)

    class Meta:
        abstract = True


class Professor(Pessoa):
    titulacao = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.matricula} - {self.user.first_name}"


class Turma(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING, related_name="turma")
    turno = models.CharField(max_length=1)
    periodo = models.IntegerField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name="turma")

    def __str__(self):
        return f"{self.disciplina.nome} - {self.turno} - {self.professor.user.professor.matricula}"


class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    aval_mec = models.IntegerField()
    disciplinas = models.ManyToManyField(Disciplina, blank=True, related_name="cursos")

    def __str__(self):
        return f"{self.nome}"


class Aluno(Pessoa):
    turmas = models.ManyToManyField(Turma, through='Turma_Aluno')
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True, related_name="aluno")

    def __str__(self):
        return f"{self.matricula} - {self.user.first_name}"


class Turma_Aluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


class Chamada(models.Model):
    presenca = models.BooleanField()
    data = models.DateField()
    turma_aluno = models.ForeignKey(Turma_Aluno, on_delete=models.CASCADE)

