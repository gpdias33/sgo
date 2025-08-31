from django import forms
from . import models

class TipoRiscoForm(forms.ModelForm):
    class Meta:
        model = models.TipoRisco
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
        }