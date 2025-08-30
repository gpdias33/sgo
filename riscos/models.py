from django.db import models
from tiposriscos.models import TipoRisco

# Create your models here.
class Risco(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    tiporisco = models.ForeignKey(TipoRisco, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'risco'