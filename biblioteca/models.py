from django.db import models   
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import date 

class Autor(models.Model):
    name = models.CharField(max_length=120, validators=[MinLengthValidator(3)])
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
    autor = models.ManyToManyField(Autor, related_name="books")
    categories = models.ManyToManyField(Category, blank=True)
    ano_publicacao = models.PositiveIntegerField(validators=[MinLengthValidator(1450), MaxLengthValidator(date.today().year)])
    disponivel = models.BooleanField(default=True)
    num_paginas = models.PositiveIntegerField(null=True, blank=True, validators=[MinLengthValidator(1), MaxLengthValidator(5000)])
    isbn = models.CharField(max_length=13, null=True, blank=True, validators=[MinLengthValidator(13), MaxLengthValidator(13)])

    def __str__(self):
        return self.titulo