from django import forms
from . import models

class ExameForm(forms.ModelForm):
    class Meta:
        model = models.Exame
        fields = ['nome', 'validade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'validade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
            'validade': 'Validade(dias)',
        }