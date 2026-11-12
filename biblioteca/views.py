from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Autor
from .forms import AutorForm

def list_livros(request):
    livros = Livro.objects.all()

    context = {
        "livros": livros
    }

    return render(request, "biblioteca/list_livros.html", context)

def create_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            return redirect("autor", id=autor.id)
    else:
        form = AutorForm()
    
    context = {
        "form": form
    }
    return render(request, "biblioteca/create_autor.html", context)


def autor_detail(request, id):
    autor = get_object_or_404(Autor, id=id)

    livros = autor.books.all()

    context = {
        "autor": autor,
        "livros": livros
    }

    return render(request, "biblioteca/autor_detail.html", context)