from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"

        labels = {
            "name": "Nome",
            "nationality": "Nacionalidade"
        }