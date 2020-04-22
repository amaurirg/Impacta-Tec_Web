from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=120)

    # quem será o tipo de campo de usuário
    USERNAME_FIELD = "email"
    # campos obrigatórios
    REQUIRED_FIELDS = ["nome"]

    # o AbstractBaseUser não tem objects, então devemos criar um
    # UserManager interface de usuário com o DB para salvar, alterar, entre outras coisas
    objects = UserManager()

    # precisamos informar ao Django qual AUTH_USER_MODEL, em settings.py
    # AUTH_USER_MODEL = "contas.Usuario"
