from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_livros, name="livros"),
    path('<int:id>/', views.autor_detail, name="autor")
]
