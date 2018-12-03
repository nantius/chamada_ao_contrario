from django.http import HttpResponseRedirect,  JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from chamada.models import Turma, Professor, TurmaAluno, Chamada, Presenca
from django.utils import timezone
import datetime

# Create your views here.


def index(request):

    if request.user.is_authenticated:
        # Verifica se o usuário é um professor ou aluno
        professor = Professor.objects.filter(user_id=request.user.id)

        context = {
            "user": request.user
        }

        if professor:
            context['professor'] = True
        else:
            context['professor'] = False

        return render(request, "index.html", context)
    return render(request, "index.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, "users/login.html", {"message": "Invalid Credentials"})
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

# Função de registro
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def professor_chamada(request):

    # Verifica se o usuário é um professor
    professor = Professor.objects.filter(user_id=request.user.id)

    # Caso não seja um professor manda para a página principal
    if not professor:
        return redirect('index')

    # Puxando as turmas onde este professor é o encarregado
    turmas = Turma.objects.filter(professor__user_id=request.user.id)

    # Puxando chamadas ativas
    chamadas = Chamada.objects.filter(ativa=True)

    context = {}

    if chamadas:
        context['chamadas'] = chamadas

    if turmas:
        context['turmas'] = turmas

    return render(request, 'professor/chamadas.html', context)


def aluno_chamada(request):

    # Busca todas as presenças de chamadas ativas, deste aluno e que ainda não foram marcadas presente
    turmas = Presenca.objects.filter(chamada__ativa=True, turma_aluno__aluno__user_id__exact=request.user.id, presenca=False).distinct()

    context = {}

    if turmas:
        context['presencas'] = turmas

    return render(request, 'chamadas.html', context)


def desativar_chamada(request, id):
    Chamada.objects.filter(id=id).update(ativa=False)
    return redirect('professor_chamada')


def marcar_presenca(request, id):
    Presenca.objects.filter(id=id).update(presenca=True)
    return redirect('aluno_chamada')


def nova_chamada(request):

    if request.method != 'POST':
        return redirect('index')

    # Resgatando valor enviado por post
    turma_id = request.POST["turma"]

    # Pegando todas as referencias para alunos
    turmas = TurmaAluno.objects.filter(turma_id=turma_id)

    # Criação da chamada
    chamada = Chamada(data=timezone.now(), ativa=True)
    chamada.save()

    # Criação da presença
    for turma in turmas:
        presenca = Presenca(turma_aluno=turma, chamada=chamada, presenca=False)
        presenca.save()

    return redirect('professor_chamada')

