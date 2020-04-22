from django.shortcuts import render


def index(request):
    context = {
        "titulo": "Faculdade Impacta"
    }
    return render(request, "index.html", context)

def cursos(request):
    context = {
        "titulo": "Lista de Cursos",
        "cursos": [
            {
                "nome": "Análise e Desenvolvimento de Sistemas",
                "sigla": "ADS",
                "descricao": "Descrição de ADS"
            },
            {
                "nome": "Sistemas de Informação",
                "sigla": "SI",
                "descricao": "Descrição de SI"
            },
            {
                "nome": "Banco de Dados",
                "sigla": "BD",
                "descricao": "Descrição de BD"
            },
            {
                "nome": "Gestão de Projetos",
                "sigla": "GP",
                "descricao": "Descrição de GP"
            },
        ]
    }
    return render(request, "cursos.html", context)
