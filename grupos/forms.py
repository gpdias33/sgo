from django import forms
from . import models

class GrupoForm(forms.ModelForm):
    class Meta:
        model = models.Grupo
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
        }