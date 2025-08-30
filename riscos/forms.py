from django.forms import ModelForm
from .models import Risco

class RiscoForm(ModelForm):
    class Meta:
        model= Risco
        fields = '__all__'