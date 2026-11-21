from django import forms
from datetime import date
from .models import Autor, Livro, Category

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"

        labels = {
            "name": "Nome",
            "nationality": "Nacionalidade"
        }

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = [
            "titulo",
            "autor",
            "ano_publicacao",
            "disponivel",
            "categories",
            "num_paginas",
            "isbn",
            "capa"
        ]

        labels = {
            "titulo": "Título",
            "autor": "Autor(es)",
            "ano_publicacao": "Ano de publicação",
            "disponivel": "Disponível",
            "categories": "Categorias",
            "num_paginas": "Número de páginas",
            "isbn": "ISBN",
            "capa": "Capa"
        }


    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"]
        titulo = " ".join(titulo.split())

        if len(titulo) < 3:
            raise forms.ValidationError(
                "O título precisa ter pelo menos 3 caracteres."
            )

        return titulo

    def clean_ano_publicacao(self):
        ano = self.cleaned_data["ano_publicacao"]

        if ano > date.today().year:
            raise forms.ValidationError(
                "O ano não pode ser posterior ao ano atual."
            )

        return ano
