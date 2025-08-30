from django.forms import ModelForm
from .models import TipoExame

class TipoExameForm(ModelForm):
    class Meta:
        model= TipoExame
        fields = '__all__'