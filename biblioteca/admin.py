from django.contrib import admin
from .models import Livro, Autor, Category

class LivroInline(admin.TabularInline):
    model = Livro.autor.through
    extra = 1

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "listar_autores", "ano_publicacao", "disponivel"]
    search_fields = ["titulo", "autor__name"]
    list_filter = ["categories", "disponivel"]
    filter_horizontal = ["categories", "autor"]

    @admin.display(description="Autores")
    def listar_autores(self, obj):
        return ", ".join(
            autor.name for autor in obj.autor.all()
        )

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    inlines= [LivroInline]

admin.site.register(Category)