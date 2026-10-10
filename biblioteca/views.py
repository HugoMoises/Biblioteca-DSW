from django.shortcuts import render
from .models import Livro

def list_livros(request):
    livros = Livro.objects.all()

    context = {
        "livros": livros
    }

    return render(request, "biblioteca/list_livros.html", context)
