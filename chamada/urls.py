from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registro", views.signup, name="signup"),
    path("professor", views.professor_chamada, name="professor_chamada"),
    path("nova_chamada", views.nova_chamada, name="nova_chamada"),
    path("chamadas", views.aluno_chamada, name="aluno_chamada"),
    path("desativar_chamada/<int:id>", views.desativar_chamada, name="desativar_chamada"),
    path("marcar_presenca/<int:id>", views.marcar_presenca, name="marcar_presenca")
]