from django.contrib import admin
from .models import Aluno, Disciplina, Curso, Professor, Chamada, Turma, Turma_Aluno

# Register your models here.


class TurmaAlunoInline(admin.TabularInline):
    model = Turma_Aluno
    extra = 5

class AlunoAdmin(admin.ModelAdmin):
    inlines = (TurmaAlunoInline,)

class TurmaAdmin(admin.ModelAdmin):
    inlines = (TurmaAlunoInline,)


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Chamada)



