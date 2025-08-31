from django import forms
from . import models

class RiscoForm(forms.ModelForm):
    class Meta:
        model = models.Risco
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
        }