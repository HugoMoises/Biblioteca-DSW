from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name        

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="books")
    ano_publicacao = models.IntegerField()
    categories = models.ManyToManyField(Category, blank=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo