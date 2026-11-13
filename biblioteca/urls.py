from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_livros, name="livros"),
    path('autor/<int:id>/', views.autor_detail, name="autor"),
    path("autor/criar/", views.create_autor, name="create-autor"),
    path("livro/criar/", views.create_edit_livro, name="livro-criar"),
    path("livro/<int:pk>/editar/", views.create_edit_livro, name="livro-editar")
]
