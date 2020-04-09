from django.shortcuts import render


def olaMundo(request):
    return render(request, "index.html")
