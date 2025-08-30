from django.forms import ModelForm
from .models import TipoRisco

class TipoRiscoForm(ModelForm):
    class Meta:
        model= TipoRisco
        fields = '__all__'