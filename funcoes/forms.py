from django import forms
from . import models

class FuncaoForm(forms.ModelForm):
    class Meta:
        model = models.Funcao
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
        }