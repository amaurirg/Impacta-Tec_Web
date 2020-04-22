from django.shortcuts import render


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


def curso(request, sigla):
    dados = {
        "SI": {
            "nome": "Sistemas de Informação",
            "sigla": "SI",
            "sobre": "Descrição de SI",
            "periodo": ["Matutino", "Noturno"]
        },
        "ADS": {
            "nome": "Análise e Desenvolvimento de Sistemas",
            "sigla": "ADS",
            "sobre": "Descrição de ADS",
            "periodo": ["Matutino", "Noturno"],
            "duracao": "4 semestres"
        }
    }
    context = {
        "curso": dados[sigla]
    }
    return render(request, 'curso.html', context)
