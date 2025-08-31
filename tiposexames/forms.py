from django import forms
from . import models

class TipoExameForm(forms.ModelForm):
    class Meta:
        model = models.TipoExame
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
        }