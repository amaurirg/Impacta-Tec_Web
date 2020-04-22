from django.shortcuts import render

from cursos.models import Curso


def cursos(request):
    context = {
        "titulo": "Lista de Cursos",
        "cursos": Curso.objects.all()
    }
    return render(request, "cursos.html", context)


def curso(request, sigla):
    curso = Curso.objects.get(sigla=sigla)
    context = {
        "curso": curso
    }
    return render(request, 'curso.html', context)
