from django.contrib import admin
from .models import Aluno, Disciplina, Curso, Professor, Chamada

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Chamada)

