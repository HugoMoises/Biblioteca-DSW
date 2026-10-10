from django.shortcuts import render, get_object_or_404
from .models import Livro, Autor

def list_livros(request):
    livros = Livro.objects.all()

    context = {
        "livros": livros
    }

    return render(request, "biblioteca/list_livros.html", context)

def autor_detail(request, id):
    autor = get_object_or_404(Autor, id=id)

    livros = autor.books.all()

    context = {
        "autor": autor,
        "livros": livros
    }

    return render(request, "biblioteca/autor_detail.html", context)