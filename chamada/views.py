from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from chamada.models import Turma, Professor

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user
        }
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

    if turmas:
        context = {
            'turmas': turmas
        }
    else:
        context = {
            turmas: 'vazio'
        }

    return render(request, 'professor/chamadas.html', context)
