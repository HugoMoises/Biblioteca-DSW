
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView 
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from .models import Livro, Autor
from .forms import AutorForm, LivroForm


class LivroListView(ListView):
    model = Livro
    template_name = "biblioteca/list_livros.html"
    context_object_name = "livros"
    queryset = Livro.objects.order_by("titulo")


class LivroFormMixin:
    success_url = reverse_lazy("livros")

    def get_success_url(self):
        next_url = self.request.POST.get("next")

        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={self.request.get_host()}
        ):
            return next_url

        return super().get_success_url()


class LivroCreateView(LivroFormMixin, CreateView):
    model = Livro
    form_class = LivroForm
    template_name = "biblioteca/form_livro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Novo livro"
        context["botao"] = "Cadastrar livro"
        context["next"] = self.request.GET.get("next", "")
        return context


class LivroUpdateView(LivroFormMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = "biblioteca/form_livro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar livro"
        context["botao"] = "Salvar alterações"
        context["next"] = self.request.GET.get("next", "")
        return context


class LivroDeleteView(DeleteView):
    model = Livro
    template_name = "biblioteca/livro_confirm_delete.html"
    success_url = reverse_lazy("livros")


class SobreView(TemplateView):
    template_name = "biblioteca/sobre.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_livros"] = Livro.objects.count()
        context["livros_disponiveis"] = Livro.objects.filter(
            disponivel=True
        ).count()
        return context


def create_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            return redirect("autor", id=autor.id)
    else:
        form = AutorForm()

    return render(request, "biblioteca/create_autor.html", {
        "form": form
    })


def autor_detail(request, id):
    autor = get_object_or_404(Autor, id=id)
    livros = autor.books.all()

    return render(request, "biblioteca/autor_detail.html", {
        "autor": autor,
        "livros": livros
    })
