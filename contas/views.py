from django.shortcuts import render, redirect
from contas.models import Usuario
from django.contrib.auth import login, authenticate

def registrar(request):
    if request.POST:
        email = request.POST.get("email")
        nome = request.POST.get("nome")
        senha = request.POST.get("password")
        senha2 = request.POST.get("password2")

        if senha == senha2:
            usuario = Usuario()
            usuario.email = email
            usuario.nome = nome
            # método do AbstractBaseUser para criptografar a senha
            usuario.set_password(senha)
            usuario.save()
            authenticate(username=usuario.email, password=senha)
            login(request, usuario)
            return redirect("home")
    else:
        return render(request, 'registrar.html')

