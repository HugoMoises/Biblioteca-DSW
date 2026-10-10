from django.contrib import admin
from .models import Livro, Autor, Category

class LivorInline(admin.TabularInline):
    model = Livro
    extra = 1

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "ano_publicacao", "disponivel"]
    search_fields = ["titulo", "autor__name"]
    list_filter = ["categories", "disponivel"]
    filter_horizontal = ["categories"]

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    inlines= [LivorInline]

admin.site.register(Category)