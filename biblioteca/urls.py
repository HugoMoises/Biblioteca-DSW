from django.urls import path
from . import views

urlpatterns = [
    path("", views.LivroListView.as_view(), name="livros"),
    path("livros/novo/", views.LivroCreateView.as_view(), name="livro-criar"),
    path("livros/<int:pk>/editar/", views.LivroUpdateView.as_view(), name="livro-editar"),
    path("livros/<int:pk>/excluir/", views.LivroDeleteView.as_view(), name="livro-excluir"),
    path("sobre/", views.SobreView.as_view(), name="sobre"),
    path('autor/<int:id>/', views.autor_detail, name="autor"),
    path("autor/criar/", views.create_autor, name="create-autor"),

]
