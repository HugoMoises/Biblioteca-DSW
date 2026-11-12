from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_livros, name="livros"),
    path('autor/<int:id>/', views.autor_detail, name="autor"),
    path("create/", views.create_autor, name="create-autor")
]
