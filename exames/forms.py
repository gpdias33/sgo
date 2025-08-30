from django.forms import ModelForm
from .models import Exame

class ExameForm(ModelForm):
    class Meta:
        model= Exame
        fields = '__all__'
