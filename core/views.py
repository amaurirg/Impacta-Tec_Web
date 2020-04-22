from django.shortcuts import render


def index(request):
    context = {
        "titulo": "Faculdade Impacta"
    }
    return render(request, "index.html", context)
