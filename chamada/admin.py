from django.contrib import admin
from .models import Aluno, Disciplina, Curso, Professor, Chamada, Turma, TurmaAluno, Presenca

# Register your models here.


class TurmaAlunoInline(admin.TabularInline):
    model = TurmaAluno
    extra = 5

class PresencaInline(admin.TabularInline):
    model = Presenca
    extra = 5

class AlunoAdmin(admin.ModelAdmin):
    inlines = (TurmaAlunoInline,)

class TurmaAdmin(admin.ModelAdmin):
    inlines = (TurmaAlunoInline,)

class ChamadaAdmin(admin.ModelAdmin):
    inlines = (PresencaInline,)


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Chamada, ChamadaAdmin)



